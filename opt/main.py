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
def recordData(DB:list):
            while True:
                print("\n"+"YYYYMMDD","\n")
                date_tmp=input()
                print("storeName","\n")
                store_tmp=input()
                print("price","\n")
                price_tmp=input()
                print("class","\n")
                class_tmp=input()
                print("date: ",date_tmp,"\n","store: ",store_tmp,"\n","price: ",price_tmp,"\n","class: ",class_tmp,"\n","OK? Y/n","\n")
                if input()=="Y":
                    DB.append([date_tmp,store_tmp,price_tmp,class_tmp])
                    print("complete!","\n")
                else:
                    print("cancel","\n")

# #search
# def searchData():

# #budget
# def budget():


#DBの表示
def showDB(db:list):
    print(tab(db,headers=['date','name','price','class'],tablefmt='github',numalign='left'))


#lineの表示
def printLine():
    print("------------------------------------------------------------------------")

def main():
    DB:list=preReaderDB()
    while True:
        printLine()
        print("Hello!","\n","please select option","\n","|record|search|budget|show|=end=|")
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
            #showメソッドの実装
            showDB(DB)
        elif option=="quit" or option=="exit" or option=="end":
            break
        else :
            print("\n","Error:option is not true","\n")
            continue

if __name__=="__main__":
    main()
