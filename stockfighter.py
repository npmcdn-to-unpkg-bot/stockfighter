import json
import time

from six.moves.urllib.parse import urljoin
import requests


class Stockfighter:
    base_url = "https://api.stockfighter.io/ob/api/"

    def __init__(self, venue, account, api_key=None):
        self.venue = venue
        self.account = account
        self.api_key = api_key
        self.headers = {
            "X-Starfighter-Authorization": api_key,
            "User-Agent": "homunculus",
        }

    def _get(self, *args, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        else:
            kwargs["headers"] = kwargs["headers"]
        return requests.get(*args, **kwargs)

    def _post(self, *args, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        else:
            kwargs["headers"] = kwargs["headers"]
        return requests.post(*args, **kwargs)

    def get_orderbook(self, stock):
        url = urljoin(
            self.base_url,
            "venues/{0}/stocks/{1}".format(
                self.venue,
                stock,
            ))
        response = self._get(url)
        return response

    def get_latest_quote(self, stock):
        url = urljoin(
            self.base_url,
            "venues/{0}/stocks/{1}/quote".format(
                self.venue,
                stock,
            ))
        response = self._get(url)
        return response

    def place_order(self, **kwargs):
        data = {
            "account": self.account,
            "venue": self.venue,
            "stock": kwargs.get("stock", None),
            "price": kwargs.get("price", None),
            "qty": kwargs.get("quantity", None),
            "direction": kwargs.get("direction", None),
            "orderType": kwargs.get("order_type", None),
        }
        url = urljoin(
            self.base_url,
            "venues/{0}/stocks/{1}/orders".format(
                self.venue,
                kwargs.get("stock"),
            ))
        response = self._post(url, json=data)
        return response

    def stats(self, quote):
        if "ask" in quote and "bid" in quote:
            bid_ask_spread = quote["ask"] - quote["bid"]
        else:
            bid_ask_spread = None
        return {
            "bid_ask_spread": bid_ask_spread
        }

    def list_order_types(self):
        order_types = [
            "limit",
            "immediate-or-cancel",
            "fill-or-kill",
            "market",
        ]
        print(order_types)
