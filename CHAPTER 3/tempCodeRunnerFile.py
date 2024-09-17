import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ["Sữa","Bánh mì","Trứng","Phở"],
    ["Bánh mì", "Bơ"],
    ["Sữa","Bánh mì","Bơ","Hành tây"],
    ["Sữa","Bánh mì","Bơ"],
    ["Bánh mì","Trứng"]
]

transactions.to_csv('data.csv',index = False)


