import pyupbit
import requests

def buy_market_order(coin_name):
    coin = 'KRW-'+coin_name
    price = pyupbit.get_current_price(coin)
    print(price)

    # access_key = ""
    # secret_key = ""

    upbit = pyupbit.Upbit(access_key, secret_key)
    my_balance = upbit.get_balances()[0]['balance']
    print(my_balance)

    ret = upbit.buy_limit_order(coin, price, '{0:.2f}'.format(my_balance/price*1.1))
    print(ret)