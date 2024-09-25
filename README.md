# 家計簿

## 仕様
使用言語はpython \
csvをデータベースとして用いる．



## 機能
### 書き込み 
日付，店名，価格，支払方法，分類のレコードを作成し，DB.csvに書き込む
 * 日付
 西暦/月/日　の形で書き込む．
 > カレンダー形式で入力できたら便利だな
 * 店名\
 レシートの店名を書き込む.
 > OCRできたらヤバイ．
 * 価格
 * 支払方法\
 クレジットor現金
 * 分類\
 自由予算or貸付予算
 
---
### 検索 
日付,店名にて検索できるようにする．
---
### 整合性チェック 
入力したレコードが決済履歴と合致しているのかを手動にて確認できるようにする． \
合致していないレコードのピックアップ機能を追加予定．
---
### 予算 
今月の自由利用予算と利用残高を確認できるようにする.