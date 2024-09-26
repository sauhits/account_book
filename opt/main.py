import csv
import pandas as pd
import pprint

def preReaderDB():
    DB=pd.read_csv("book.csv",header=None).values.tolist()
    # print(DB)
    return DB

#データの記録　20000101,カネスエ,XXXX,free(loan)
def recordData(DB):
            while True:
                print("\n"+"YYYYMMDD"+"\n")
                date_tmp=input()
                print("storeName"+"\n")
                store_tmp=input()
                print("price"+"\n")
                price_tmp=input()
                print("class"+"\n")
                class_tmp=input()
                print("date: "+date_tmp+"\n"+"store: "+store_tmp+"\n"+"price: "+price_tmp+"\n"+"class: "+class_tmp+"\n"+"OK? Y/n"+"\n")
                if input()=="Y":
                    DB.append([date_tmp,store_tmp,price_tmp,class_tmp])
                    print("complete!"+"\n")
                else:
                    print("cancel"+"\n")

def main():
    DB=preReaderDB()
    while True:
        print("Hello!"+"\n"+"please select option"+"\n"+"|record|search|budget|")
        option=input()
        if option!="record" and option!="search" and option!="budget":
            print("\n"+"Error:option is not true"+"\n")
            continue
        if option=="record":
            recordData(DB)
        

if __name__=="__main__":
    main()
