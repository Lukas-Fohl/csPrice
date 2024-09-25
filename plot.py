from datetime import *

class dataClass:
    price: float
    time: int
    def __init__(self, priceIn: str, timeIn) -> None:
        self.time = timeIn
        self.price = priceIn.replace(",",".")
        self.price = float(self.price[:len(self.price)-1])
        pass

def readData(pathIn: str):
    returnArray = []
    minTime = 0
    with open(pathIn) as dataFile:
        dataArray = dataFile.read().split("\n")
        minTime = datetime.fromtimestamp(int((dataArray[0].split('#')[0])))
        for i in dataArray:
            if len(i.split("#")) > 1:
                tempPrice = i.split("#")[1]
                timeNow = datetime.fromtimestamp(int(i.split("#")[0]))
                tempTime = (timeNow - minTime).total_seconds() / 60 / 60
                returnArray.append(dataClass(tempPrice, tempTime))
    return returnArray

def main():
    import matplotlib.pyplot as plt

    x = []
    y = []

    for i in readData("./data.txt"):
        y.append(i.price)
        x.append(i.time)

    plt.plot(x, y)

    plt.xlabel('time - in hours')
    plt.ylabel('price - €')

    plt.title('Donk sticker plot')

    plt.show()
    return

main()