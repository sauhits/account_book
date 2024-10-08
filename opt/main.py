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
    return afterDB


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


# delete
def deleteData(db: list):
    while True:
        showDB(db)
        print("RECORD NUMBER ?\n")
        try:
            targetIndex = int(input())
        except (IndexError, ValueError):
            print("Fail Index Number\n")
            continue
        else:
            printLine()
            tmpDB = [
                db[targetIndex]["date"],
                db[targetIndex]["name"],
                db[targetIndex]["price"],
                db[targetIndex]["type"],
            ]
            print(tmpDB)
            print("Y/n ?\n")
            if input() == "y" or "Y":
                db.remove(db[targetIndex])
            print("complete!")
            return db


# search
def searchData(db: list, yyyymm, name, type):
    afterDB = []
    if yyyymm != "any":
        fromDate = int(yyyymm) * 100
        toDate = int(yyyymm) * 100 + 31
        for targetData in db:
            if fromDate <= targetData["date"] <= toDate:
                afterDB.append(targetData)
    else:
        for targetData in db:
            afterDB.append(targetData)
    if name != "any":
        for targetData in afterDB:
            if targetData["name"] != name:
                afterDB.remove(targetData)
    if type != "any":
        for targetData in afterDB:
            if targetData["type"] != type:
                afterDB.remove(targetData)
    return afterDB


# DBの表示
def showDB(db: list):
    tmpDB = []
    for data in db:
        tmpDB.append([data["date"], data["name"], data["price"], data["type"]])
    print(
        tab(
            tmpDB,
            headers=["date", "name", "price", "type"],
            tablefmt="github",
            numalign="left",
            showindex=True,
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
        if type == data_price["type"]:
            SUM_tmp += int(data_price["price"])
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
            + "\n\nplease select option\n| INCOME | EXPENDITURE | SHOW | SEARCH | DELETE | QUIT |"
        )
        printLine()
        option: str = input().lower()

        # 選択肢フィルター
        # income
        if option == "income":
            recordData(IncomeDB)
        # expenditure
        elif option == "expenditure":
            recordData(ExpenditureDB)
        # show
        elif option == "show":
            printLine()
            print("INCOME HISTORY")
            showDB(IncomeDB)
            printLine()
            print("EXPENDITURE HISTORY")
            showDB(ExpenditureDB)
        # search
        elif option == "search":
            print("\nINCOME or EXPENDITURE\n")
            targetDB = input()
            printLine()
            print("YYYYMM ?")
            targetDate = input()
            printLine()
            print("NAME ?")
            targetName = input()
            printLine()
            print("TYPE ?")
            targetType = input()
            printLine()
            if targetDB == "income":
                showDB(searchData(IncomeDB, targetDate, targetName, targetType))
            else:
                showDB(searchData(ExpenditureDB, targetDate, targetName, targetType))
        # delete
        elif option == "delete":
            print("\nINCOME or EXPENDITURE\n")
            targetDB = input()
            printLine()
            if targetDB.lower == "income":
                IncomeDB = deleteData(IncomeDB)
            else:
                IncomeDB = deleteData(ExpenditureDB)
        # quit
        elif option == "quit" or option == "exit" or option == "end" or option == "q":
            break
        else:
            print("\nError:option is not true\n")
            continue


if __name__ == "__main__":
    main()
