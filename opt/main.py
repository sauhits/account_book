import csv
import pandas as pd
import pprint
from tabulate import tabulate as tab

#データの読み込み
def preReaderDB():
    DB:list=pd.read_csv("book.csv",header=None).values.tolist()
    # print(DB)
    return DB

#データの記録　20000101,カネスエ,XXXX,free(loan)
def recordData(db:list):
    while True:
        print("\n"+"YYYYMMDD","\n")
        date_tmp=input()
        if date_tmp=="q":
            return
        printLine()
        print("storeName","\n")
        store_tmp=input()
        if store_tmp=="re":
            continue
        printLine()
        print("price","\n")
        price_tmp=input()
        if price_tmp=="re":
            continue
        printLine()
        print("class","\n")
        class_tmp=input()
        if class_tmp=="re":
            continue
        printLine()
        print("\n","date: ",date_tmp,"\n","store: ",store_tmp,"\n","price: ",price_tmp,"\n","class: ",class_tmp,"\n","\n","OK? Y/n","\n")
        if input()=="Y"or"y":
            insertDataToDB(db,[date_tmp,store_tmp,price_tmp,class_tmp])
            print("complete!","\n")
        else:
            print("cancel","\n")

#insert
def insertDataToDB(db:list,data:list):
    for num_tmp,dateInDB in enumerate(db):
        if int(dateInDB[0]) > int(data[0]):
            db.insert(num_tmp,data)
            return
    db.append(data)


# #search
# def searchData():

# #budget
# def budget():


#DBの表示
def showDB(db:list):
    print(db)
    print(tab(db,headers=['date','name','price','class'],tablefmt='github',numalign='left'))

#データの表示
def showData(data:list):
    print(tab(data,headers=['date','name','price','class'],tablefmt='github',numalign='left'))

#lineの表示
def printLine():
    print("-----------------------------------------")

def main():
    DB:list=preReaderDB()
    while True:
        printLine()
        print("Hello!","\n","please select option","\n","|record|search|budget|show|delete|quit|")
        printLine()
        option:str=input()
        #選択肢フィルター            
        if option=="record":
            recordData(DB)
        # elif option=="search":
        #     #searchメソッドの実装
        #     search()
        # elif option=="budget":
        #     #budgetメソッドの実装
            
        elif option=="show":
            showDB(DB)
        elif option=="quit" or option=="exit" or option=="end" or option=="q":
            break
        else :
            print("\n","Error:option is not true","\n")
            continue

if __name__=="__main__":
    main()
