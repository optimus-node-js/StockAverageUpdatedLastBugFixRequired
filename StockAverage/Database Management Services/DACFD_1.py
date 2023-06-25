"""Delete All the Collections from the Database"""
from subprocess import getstatusoutput

import pyautogui
import pymongo
import colorama
from colorama import Fore
import threading
from time import sleep

theCollections = ['eachStockData', 'todaySumData', 'averageData']


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


def deleteDataBaseCollection(collectionName, confirm=False):
    global collection
    if confirm:
        clientI = pymongo.MongoClient(
            "mongodb+srv://rahul_vvishwakarma:***REDACTED***@cluster1.zrhednl.mongodb.net/?retryWrites=true&w=majority")
        db = clientI['TradeCollection'][collectionName]
        collectionCount = db.delete_many({})

    print(f"\033[1m[ {str(collectionCount.deleted_count)} ] + \tdocuments are Deleted from [{collectionName}]")


def authentication():
    keyPass = False

    msg = "\033[1m  [1]  eachStockData Collection\t" \
          "\033[1m  [2]  todaySumData Collection\t" \
          "\033[1m  [3]  averageData Collection\t\t\t" \
          "\033[1m  [4]  Clear all collection documents\t\t\n\n"

    print_msg_box(msg=msg, indent=2, title='Choose the Option:')
    collectionType = int
    while True:
        collectionType = ((int(input("\n\033[1mWhich Collection you want to delete : "))) - 1)
        if collectionType > 4:
            print("\033[1m<Choose Option Among 1-2-3-4 >")
        else:
            break

    while not keyPass:
        for i in range(1, 4):
            password = input(f"{Fore.LIGHTWHITE_EX}\033[1mEnter the passKey : ")
            print(f"{Fore.WHITE}Authenticating...")

            client = pymongo.MongoClient(
                "mongodb+srv://rahulVishwakarma:***REDACTED***@cluster0.s0kvxoz.mongodb.net/?retryWrites=true&w=majority")
            dbCollection = client['BelgiumServer']['SecurityConfirmation']
            res = [items for items in dbCollection.find({}, {"_id": 0})]

            authenticationKey = res[0]["DeleteAllData"]

            if password == authenticationKey:
                print(f"{Fore.GREEN}Authentication Successful✅\n")
                keyPass = True

                if collectionType < 3:
                    deleteDataBaseCollection(theCollections[collectionType], True)
                if collectionType == 3:
                    thread1 = threading.Thread(target=deleteDataBaseCollection(theCollections[0], True))
                    thread2 = threading.Thread(target=deleteDataBaseCollection(theCollections[1], True))
                    thread3 = threading.Thread(target=deleteDataBaseCollection(theCollections[2], True))

                    thread1.start()
                    thread2.start()
                    thread3.start()

                    thread1.join()
                    thread2.join()
                    thread3.join()

                break

            else:
                print(f"Substantiate Failed ❌ \t\tAttempts Left-{4 - i}")


def mainStart():
    colorama.init(autoreset=True)
    icDisconnectCount = 0
    while True:
        InternetStatus = int((getstatusoutput('ping -n 2 www.google.com >nul && echo 0 || echo 1'))[1])
        if InternetStatus == 0:
            if icDisconnectCount > 0:
                pyautogui.hotkey('shift', 'F10')
            print("Internet Connected ✅")
            authentication()
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
