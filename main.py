import urllib
import json
import urllib.request
import time
from datetime import datetime
from upbit import buy_market_order

if __name__ == '__main__':
    while True:
        try:
            url = 'https://project-team.upbit.com/api/v1/disclosure?region=kr&per_page=10'

            html=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html1=urllib.request.urlopen(html)
            json1=json.load(html1)
            notice=json1['data']['posts'][0]['text']
            new_coin=json1['data']['posts'][0]['assets']
            latest_coin=''

            if latest_coin != new_coin:
                latest_coin = new_coin

                if notice.find('카카오')!=-1:
                    buy_market_order(new_coin)
                if notice.find('구글')!=-1:
                    buy_market_order(new_coin)
        except:
            print(" ")

        time.sleep(1)
    print(latest_coin, datetime.now())