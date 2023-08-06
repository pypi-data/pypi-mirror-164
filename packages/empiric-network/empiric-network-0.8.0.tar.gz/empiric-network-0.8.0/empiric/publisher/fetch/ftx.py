import datetime
import hmac
import logging
import os
import re
import time
from typing import List

import requests
from empiric.core.entry import Entry
from empiric.core.utils import currency_pair_to_key

logger = logging.getLogger(__name__)


def parse_ftx_spot(asset, data, source, publisher, timestamp) -> Entry:
    pair = asset["pair"]
    key = currency_pair_to_key(*pair)

    result = [e for e in data if e["name"] == "/".join(pair)]
    if len(result) == 0:
        logger.debug(f"No entry found for {'/'.join(pair)} from FTX")
        return

    assert (
        len(result) == 1
    ), f"Found more than one matching entries for FTX response and price pair {pair}"
    price = float(result[0]["price"])
    price_int = int(price * (10 ** asset["decimals"]))

    logger.info(f"Fetched price {price} for {'/'.join(pair)} from FTX")

    return Entry(
        key=key,
        value=price_int,
        timestamp=timestamp,
        source=source,
        publisher=publisher,
    )


def parse_ftx_futures(asset, data, source, publisher, timestamp) -> List[Entry]:
    pair = asset["pair"]
    if pair[1] != "USD":
        logger.debug(f"Unable to fetch price from FTX for non-USD derivative {pair}")
        return

    result = [e for e in data if re.match(rf"{pair[0]}-[0-9]+", e["name"])]
    if len(result) == 0:
        logger.debug(f"No entry found for {'/'.join(pair)} from FTX")
        return

    entries = []

    for future in result:
        price = float(future["mark"])
        price_int = int(price * (10 ** asset["decimals"]))

        future_expiration_date = int(
            datetime.datetime.strptime(
                future["expiry"],
                "%Y-%m-%dT%H:%M:%S%z",
            ).strftime("%Y%m%d")
        )
        key = f"{pair[0]}/{pair[1]}-{future_expiration_date}".lower()

        logger.info(f"Fetched futures price {price} for {key} from FTX")

        entries.append(
            Entry(
                key=key,
                value=price_int,
                timestamp=timestamp,
                source=source,
                publisher=publisher,
            )
        )

    return entries


def generate_ftx_headers(endpoint):
    FTX_API_KEY = os.environ.get("FTX_API_KEY")
    FTX_API_SECRET = os.environ.get("FTX_API_SECRET")

    timestamp = int(time.time() * 1000)
    signature = hmac.new(
        FTX_API_SECRET.encode(),
        (str(timestamp) + "GET" + endpoint).encode("ascii"),
        "sha256",
    ).hexdigest()
    headers = {
        "FTX-KEY": FTX_API_KEY,
        "FTX-SIGN": signature,
        "FTX-TS": str(timestamp),
    }
    return headers


def fetch_ftx(assets, publisher) -> List[Entry]:
    source = "ftx"
    base_url = "https://ftx.com/api"

    endpoint = "/markets"
    headers = generate_ftx_headers(endpoint)
    response = requests.get(base_url + endpoint, headers=headers, timeout=10)
    spot_data = response.json()["result"]

    endpoint = "/futures"
    headers = generate_ftx_headers(endpoint)
    response = requests.get(base_url + endpoint, headers=headers, timeout=10)
    future_data = response.json()["result"]

    timestamp = int(time.time())

    entries = []

    for asset in assets:
        if asset["type"] == "SPOT":
            entry = parse_ftx_spot(asset, spot_data, source, publisher, timestamp)
            if entry is not None:
                entries.append(entry)
            continue
        elif asset["type"] == "FUTURE":
            future_entries = parse_ftx_futures(
                asset, future_data, source, publisher, timestamp
            )
            if len(future_entries) is not None:
                entries.extend(future_entries)
            continue
        else:
            logger.debug(f"Unable to fetch FTX for un-supported asset type {asset}")

    return entries
