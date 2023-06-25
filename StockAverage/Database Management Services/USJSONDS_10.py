"""Purpose to Upload Specific or All JSON Database to Server"""
from subprocess import getstatusoutput
from time import sleep
import pyautogui
import pymongo
from os import chdir
from json import load
from threading import Thread

chdir("../")
chdir("Server DataBase JSON")

collections = ['eachStockData', 'todaySumData', 'averageData']


def jsonFilesReader(JSONfileName):
    with open(f"{JSONfileName}.json", 'r') as file:
        fileData = load(file)
        return fileData[JSONfileName]


def uploadServerModule(collectionName, arrayOfJSONdata):
    clientI = pymongo.MongoClient(
        "mongodb+srv://rahul_vvishwakarma:***REDACTED***@cluster1.zrhednl.mongodb.net/?retryWrites=true&w=majority")
    collection = clientI['TradeCollection'][collectionName]
    collection.insert_many(arrayOfJSONdata)
    print(f'\033[1m[+] {collectionName} Collection Uploaded with {len(arrayOfJSONdata)} files ️✅')


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


def engineDictate():
    msg = "\033[1m  [1]  eachStockData Collection\t" \
          "\033[1m  [2]  todaySumData Collection\t" \
          "\033[1m  [3]  averageData Collection\t\t\t" \
          "\033[1m  [4]  Download all the collection documents\t\t\n\n"

    print_msg_box(msg=msg, indent=2, title='Choose the Collection to Upload : ⬆️')

    while True:
        collectionType = ((int(input("\n\033[1mWhich Collection you want to Upload : "))) - 1)

        if collectionType > 4:
            print("\033[1m<Choose Option Among 1-2-3-4 >")
        else:
            if collectionType < 3:
                uploadServerModule(collectionType, jsonFilesReader(collectionType))

            if collectionType == 3:
                a = Thread(target=uploadServerModule(collections[0], jsonFilesReader(collections[0])))
                b = Thread(target=uploadServerModule(collections[1], jsonFilesReader(collections[1])))
                c = Thread(target=uploadServerModule(collections[2], jsonFilesReader(collections[2])))
                a.start()
                b.start()
                c.start()
                a.join()
                b.join()
                c.join()
            break


def documentsCheckerJSON_withServer(collection, JSONdata):
    clientI = pymongo.MongoClient(
        "mongodb+srv://rahul_vvishwakarma:***REDACTED***@cluster1.zrhednl.mongodb.net/?retryWrites=true&w=majority")
    collection = clientI['TradeCollection'][collection]

    # with open()
    pass


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
