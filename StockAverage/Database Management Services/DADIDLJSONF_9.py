'''Purpose is to Download Specific or All data from the Server DB to locally in JSON Format'''
from subprocess import getstatusoutput

import pyautogui
import pymongo
from threading import Thread
from os.path import exists
import os
from json import load, dump, dumps
from time import sleep

os.chdir('../')

PendingCloudDataJSON = {
    "eachStockData": [],
    "todaySumData": [],
    "averageData": []
}

if not exists("Server DataBase JSON"):
    os.mkdir("Server DataBase JSON")
    os.chdir("Server DataBase JSON")




else:
    os.chdir("Server DataBase JSON")


def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)


def downloadDataBaseCollections(collectionName, index=0):
    print(f"\033[1mDownloading {collectionName} data...⏳")
    clientI = pymongo.MongoClient(
        "mongodb+srv://rahul_vvishwakarma:***REDACTED***@cluster1.zrhednl.mongodb.net/?retryWrites=true&w=majority")
    db = clientI["TradeCollection"]

    Attribute = [{"eachStockData": []}, {"todaySumData": []}, {"averageData": []}]

    with open(f"{collectionName}.json", "w") as file:
        json_object = dumps(Attribute[index], indent=4)
        file.write(json_object)

    _collection = db[collectionName].find({}, {"_id": 0})

    newData = [item for item in _collection]

    with open(f"{collectionName}.json", 'r+') as file:
        file_data = load(file)

        for item in newData:
            file_data[f"{collectionName}"].append(item)
        file.seek(0)
        dump(file_data, file, indent=4)
    print(f"\033[1mDownload {collectionName} data ✅")


def provokeCollection(index=0):
    print(index)
    if index < 3:
        downloadDataBaseCollections(list(PendingCloudDataJSON.keys())[index], index)
    if index == 3:
        a1 = Thread(target=downloadDataBaseCollections(list(PendingCloudDataJSON.keys())[0], 0))

        a2 = Thread(target=downloadDataBaseCollections(list(PendingCloudDataJSON.keys())[1], 1))
        a3 = Thread(target=downloadDataBaseCollections(list(PendingCloudDataJSON.keys())[2], 2))
        a1.start()
        a2.start()
        a3.start()

        a1.join()
        a2.join()
        a3.join()


def engineDictate():
    msg = "\033[1m  [1]  eachStockData Collection\t" \
          "\033[1m  [2]  todaySumData Collection\t" \
          "\033[1m  [3]  averageData Collection\t\t\t" \
          "\033[1m  [4]  Download all the collection documents\t\t\n\n"

    print_msg_box(msg=msg, indent=2, title='Choose the Collection to Download:')

    while True:
        collectionType = ((int(input("\n\033[1mWhich Collection you want to Download : "))) - 1)

        if collectionType > 4:
            print("\033[1m<Choose Option Among 1-2-3-4 >")
        else:
            provokeCollection(collectionType)
            break


def mainStart():
    icDisconnectCount = 0
    while True:
        InternetStatus = int((getstatusoutput('ping -n 2 www.google.com >nul && echo 0 || echo 1'))[1])
        if InternetStatus == 0:
            if icDisconnectCount > 0:
                pyautogui.hotkey('shift', 'F10')
            print("Internet Connected ✅")
            engineDictate()
            break
        else:
            print("Please Connect to Internet 🌐")
            sleep(1.25)
            if icDisconnectCount < 2:
                icDisconnectCount += 1

            else:
                pass


if __name__ == '__main__':
    mainStart()
