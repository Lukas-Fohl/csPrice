import requests
import json
import time
import pathlib
from time import sleep

while True:
    url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20%7C%20donk%20%28Glitter%29%20%7C%20Copenhagen%202024'
    resp = requests.get(url).text
    jsonObj = json.loads(resp)
    price = jsonObj['lowest_price']
    timeStamp = int(time.time())
    with open(str(pathlib.Path(__file__).parent.resolve())+'/data.txt','+a') as dataFile:
        dataFile.write(str(timeStamp) + '#' + price + '\n')
    sleep(60 * 10)