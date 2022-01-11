## bash 17.3.2 at june
## written by monees007

import time
## TODO: Get market price at 9:20

## TODO: Round off upto 100
## TODO: Expiry Date : Earliest : Get
## TODO: Place Order : 10% STOPLOSS

import logging
from kiteconnect.connect import KiteConnect

broker_symbol = "NSE:INFY"
instrument_token = ''


logging.basicConfig(level=logging.DEBUG)
kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.generate_session("request_token_here", api_secret="your_secret")
kite.set_access_token(data["access_token"])



kite.historical_data(instrument_token,)
market_price = kite.quote(broker_symbol)["last_price"]

# Place an order
try:
    order_id = kite.place_order(tradingsymbol="INFY",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                variety=kite.VARIETY_AMO,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)

    logging.info("Order placed. ID is: {}".format(order_id))
except Exception as e:
    logging.info("Order placement failed: {}".format(e.message))