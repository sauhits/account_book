import csv
import pandas as pd
import pprint

def preReaderDB():
    DB=pd.read_csv("book.csv",header=None).values.tolist()
    # print(DB)
    return DB


def main():
    DB=preReaderDB()
    while True:
        print("Hello!"+"\n"+"please select option"+"\n"+"|record|search|budget|")
        option=input()
        if option!="record"or option!="search" or option!="budget":
            print("Error:option is not true")
            continue
        


if __name__=="__main__":
    main()
