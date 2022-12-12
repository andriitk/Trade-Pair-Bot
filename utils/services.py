import requests
from bs4 import BeautifulSoup
import random


def logic_trade(pair: str):
    URL = 'https://paper-trader.frwd.one/'

    timeframe = random.choice(['5m', '15m', '1h', '4h', '1d', '1w', '1M'])
    candles = random.randint(1, 1000)
    ma = random.randint(1, 100)
    tp = random.randint(1, 99)
    sl = random.randint(1, 99)

    response = requests.post(URL, data={'pair': pair, 'timeframe': timeframe, 'candles': candles, 'ma': ma, 'tp': tp,
                                        'sl': sl}).text

    soup = BeautifulSoup(response, "lxml")

    img_url = URL + str(soup.find('img').get('src'))

    return img_url
