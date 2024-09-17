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


te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
data = pd.DataFrame(te_array,columns=te.columns_)

frequent_itemsets = apriori(data,min_support=0.4,use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print(rules)

# print(data)
# data.to_csv('data.csv',index = False)


