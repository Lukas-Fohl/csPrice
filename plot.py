from datetime import *

class dataClass:
    price: float
    time: int
    def __init__(self, priceIn: str, timeIn) -> None:
        self.time = timeIn
        self.price = priceIn.replace(",",".")
        self.price = float(self.price[:len(self.price)-1])
        pass

def readData(pathIn: str) -> ([], float):
    returnArray = []
    minTime = 0
    startPrice = 0.0
    with open(pathIn) as dataFile:
        dataArray = dataFile.read().split("\n")
        for i in dataArray:
            if '#' in i:
                minTime = datetime.fromtimestamp(int((i.split('#')[0])))
                tempPrice = i.split("#")[1]
                tempPrice = tempPrice.replace("-","0")
                startPrice = dataClass(tempPrice,minTime).price
                break
        for i in dataArray:
            if '#' in i:
                tempPrice = i.split("#")[1]
                tempPrice = tempPrice.replace("-","0")
                timeNow = datetime.fromtimestamp(int(i.split("#")[0]))
                tempTime = (timeNow - minTime).total_seconds() / 60 / 60
                tempTime = timeNow
                returnArray.append(dataClass(tempPrice, tempTime))
    return (returnArray, (returnArray[len(returnArray)-1].price * (0.869565217391304)) - startPrice)

def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import math

    x = []
    y = []

    yredu = []

    (res, pri) = readData("/home/lukas/code/csprice/data/data1.txt")
    for i in res:
        y.append(i.price)
        yredu.append(i.price*0.95)
        x.append(i.time)

    p1 = plt.plot(x, y)

    plt.ylabel('price - €')

    plt.title('Donk sticker plot : ' + ("+" if pri > 0 else "") + str(round(pri, 2)))

    plt.show()
    return

main()
"""
plot all files
--> show date
"""