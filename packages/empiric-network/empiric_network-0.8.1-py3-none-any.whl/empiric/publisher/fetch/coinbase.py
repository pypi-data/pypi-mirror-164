import base64
import datetime
import hmac
import logging
import os
from hashlib import sha256
from typing import List

import requests
from empiric.core.entry import Entry
from empiric.core.utils import currency_pair_to_key

logger = logging.getLogger(__name__)


def fetch_coinbase(assets, publisher) -> List[Entry]:
    source = "coinbase"
    COINBASE_API_SECRET = os.environ.get("COINBASE_API_SECRET")
    COINBASE_API_KEY = os.environ.get("COINBASE_API_KEY")
    COINBASE_API_PASSPHRASE = os.environ.get("COINBASE_API_PASSPHRASE")
    URL = "https://api.exchange.coinbase.com"
    REQUEST_PATH = "/oracle"
    METHOD = "GET"

    entries = []

    for asset in assets:
        if asset["type"] != "SPOT":
            logger.debug(f"Skipping Coinbase for non-spot asset {asset}")
            continue

        pair = asset["pair"]
        key = currency_pair_to_key(*pair)

        if pair[1] != "USD":
            logger.debug(
                f"Unable to fetch Coinbase price for non-USD denomination {pair[1]}"
            )
            continue

        request_timestamp = str(
            int(
                datetime.datetime.now(datetime.timezone.utc)
                .replace(tzinfo=datetime.timezone.utc)
                .timestamp()
            )
        )

        signature = hmac.new(
            base64.b64decode(COINBASE_API_SECRET),
            (request_timestamp + METHOD + REQUEST_PATH).encode("ascii"),
            sha256,
        )

        headers = {
            "Accept": "application/json",
            "CB-ACCESS-KEY": COINBASE_API_KEY,
            "CB-ACCESS-SIGN": base64.b64encode(signature.digest()),
            "CB-ACCESS-TIMESTAMP": request_timestamp,
            "CB-ACCESS-PASSPHRASE": COINBASE_API_PASSPHRASE,
        }

        response = requests.request(
            METHOD, URL + REQUEST_PATH, headers=headers, timeout=10
        )

        response.raise_for_status()
        result = response.json()
        if pair[0] in result["prices"]:
            price = float(result["prices"][pair[0]])
            price_int = int(price * (10 ** asset["decimals"]))

            timestamp = int(result["timestamp"])

            logger.info(f"Fetched price {price} for {key} from Coinbase")

            entries.append(
                Entry(
                    key=key,
                    value=price_int,
                    timestamp=timestamp,
                    source=source,
                    publisher=publisher,
                )
            )
        else:
            logger.debug(f"No entry found for {key} from Coinbase")

    return entries
