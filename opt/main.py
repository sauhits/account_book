import pandas as pd
from tabulate import tabulate as tab


# データの読み込み
def preReaderDB(csv: str):
    afterDB = []
    DB: list = pd.read_csv(csv, header=None, encoding="shift_jis").values.tolist()
    for target in DB:
        afterDB.append(
            {
                "date": target[0],
                "name": target[1],
                "price": target[2],
                "type": target[3],
            }
        )
    # print(DB)
    return DB


# データの記録　20000101,カネスエ,XXXX,free(loan)
def recordData(db: list):
    while True:
        date_tmp = input("\nYYYYMMDD\n")
        if date_tmp == "q":
            return
        printLine()
        store_tmp = input("NAME\n")
        if store_tmp == "re":
            continue
        printLine()
        price_tmp = input("PRICE\n")
        if price_tmp == "re":
            continue
        printLine()
        type_tmp = input("TYPE\n")
        if type_tmp == "re":
            continue
        printLine()
        print(
            "\nDATE: "
            + date_tmp
            + "\nNAME: "
            + store_tmp
            + "\nPRICE: "
            + price_tmp
            + "\nTYPE: "
            + type_tmp
            + "\n"
        )
        if input("\nOK? Y/n\n") == "Y" or "y":
            insertDataToDB(db, [date_tmp, store_tmp, price_tmp, type_tmp])
            print("complete!\n")
        else:
            print("cancel\n")


# insert
def insertDataToDB(db: list, data: list):
    for num_tmp, dateInDB in enumerate(db):
        if int(dateInDB["date"]) > int(data[0]):
            db.insert(
                num_tmp,
                {"date": data[0], "name": data[1], "price": data[2], "type": data[3]},
            )
            return
    db.append({"date": data[0], "name": data[1], "price": data[2], "type": data[3]})


# DBの表示
def showDB(db: list):
    tmpDB=[]
    for data in db:
        tmpDB.append([data['date'],data['name'],data['price'],data['type']])
    print(
        tab(
            tmpDB,
            headers=["date", "name", "price", "type"],
            tablefmt="github",
            numalign="left",
        )
    )

# lineの表示
def printLine():
    print("---------------------------------------------------")


# データの金額合算の作成
def SumDBPrice(db: list, type: str):
    SUM_tmp = 0
    int
    for data_price in db:
        if type == data_price['type']:
            SUM_tmp += int(data_price['type'])
    return SUM_tmp


def main():
    # 支出データの読み込み
    ExpenditureDB: list = preReaderDB("Expenditure.csv")
    IncomeDB: list = preReaderDB("Income.csv")
    while True:
        # 予算の算出をする
        SumExpenditureOfLoan = SumDBPrice(ExpenditureDB, "loan")
        SumIncomeOfLoan = SumDBPrice(IncomeDB, "loan")
        SumExpenditureOfFree = SumDBPrice(ExpenditureDB, "free")
        SumIncomeOfFree = SumDBPrice(IncomeDB, "free")
        BalanceOfLoan = SumIncomeOfLoan - SumExpenditureOfLoan
        BalanceOfFree = SumIncomeOfFree - SumExpenditureOfFree
        printLine()
        print(
            "HELLO!\n\nBalance Loan:"
            + str(BalanceOfLoan)
            + "\n        Free:"
            + str(BalanceOfFree)
            + "\n\nplease select option\n| INCOME | EXPENDITURE |budget| SHOW |delete| QUIT |"
        )
        printLine()
        option: str = input().lower()

        # 選択肢フィルター
        if option == "income":
            recordData(IncomeDB)
        elif option == "expenditure":
            recordData(ExpenditureDB)
        elif option == "show":
            printLine()
            print("INCOME HISTORY")
            showDB(IncomeDB)
            printLine()
            print("EXPENDITURE HISTORY")
            showDB(ExpenditureDB)
        elif option == "quit" or option == "exit" or option == "end" or option == "q":
            break
        else:
            print("\nError:option is not true\n")
            continue


if __name__ == "__main__":
    main()
