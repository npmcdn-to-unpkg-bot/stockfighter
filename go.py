import argparse
import json
import random
import time

from influxdb import InfluxDBClient

import settings
import stockfighter


def stat(text, resp):
    print(text)
    print(json.dumps(resp.json(), indent=2))
    return resp.json()


def launch(account, venue, stock):
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mydb')
    sf = stockfighter.Stockfighter(
        account=args.account,
        venue=args.venue,
        api_key=settings.api_key,
    )

    sf.get_latest_quote(stock)
    sf.get_orderbook(stock)

    total_fills = 100000

    while True:
        quote = sf.get_latest_quote(stock).json()
        json_body = [
            {
                "measurement": "quote",
                "tags": {},
                "time": quote["quoteTime"],
                "fields": quote,
            }
        ]
        client.write_points(json_body)
        print(json.dumps(json_body, indent=4))

        #  qty = random.randint(1, 500)
        #  price = random.randint(3500, 3600)
        #  print("we asked for {0} at {1}".format(
        #      qty,
        #      price,
        #  ))
        #  buy_resp = sf.place_order(
        #      stock=stock,
        #      order_type="limit",
        #      quantity=qty,
        #      price=price,
        #      direction="buy",
        #  )
        #  stat("buy:", buy_resp)

        #  time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "account",
        help="Your brokerage account number",
        type=str,
    )
    parser.add_argument(
        "venue",
        help="Symbol for the stock exchange to be used",
        type=str,
    )
    parser.add_argument(
        "stock",
        help="The stock ticker symbol to be bought",
        type=str,
    )
    args = parser.parse_args()

    launch(
        account=args.account,
        venue=args.venue,
        stock=args.stock,
    )
