import requests
import json
import time
import pathlib
import os


def main():
    for i in os.walk("/home/lukas/code/csprice/data"):
        for j in i[2]:
            url = ""
            with open('/home/lukas/code/csprice/data/'+j,'r+') as readData:
                url = readData.readline().split('\n')[0]
            #url = 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20%7C%20donk%20%28Glitter%29%20%7C%20Copenhagen%202024'
            resp = requests.get(url).text
            jsonObj = json.loads(resp)
            price = jsonObj['lowest_price']
            timeStamp = int(time.time())
            with open('/home/lukas/code/csprice/data/'+j,'a') as dataFile:
                dataFile.write(str(timeStamp) + '#' + price + '\n')

main()