import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('data3.csv')
print(data)

# Simple Scaler
numColumns = data.select_dtypes(include=["int64","float64"]).columns

maxValue = data[numColumns].max()

for column in numColumns:
    data[column] = data[column] / maxValue[column]
print("Simple Scaling completed")

# Min-Max Scaler
scaler = MinMaxScaler()
numColumns = data.select_dtypes(include=['int64','float64']).columns
data[numColumns] = scaler.fit_transform(data[numColumns])
print("Min-max Scaling completed")

# # Z-Score Scaler
scaler = StandardScaler()
numColumns = data.select_dtypes(include=['int64','float64']).columns
data[numColumns] = scaler.fit_transform(data[numColumns])
print("Z-score Scaling completed")


print(data)

data.to_csv('data4.csv', index=False)

