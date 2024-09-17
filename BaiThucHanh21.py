import pandas as pd

data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

# print(data1)
# print(data2)

# Đánh giá dữ liệu

# print(data1.isna().sum())
# print(data2.isna().sum())

# print(data1[(data1['Chiều cao (cm)'] <= 0) | (data1['Cân nặng (kg)'] <= 0)])
# print(data2[(data2['Chiều cao (cm)'] <= 0) | (data1['Cân nặng (kg)'] <= 0)])

# Ho ten - Ho dem | Ten

# Xu ly tach ho ten cua Data2

# data2['Tên'] = data2['Tên'].replace(r'\d+','',regex = True)

# data2[['Đệm', 'Tên']] = data2['Tên'].apply(lambda x: pd.Series(x.split(' ', 1)))

# data2.rename(columns={'Họ đệm': 'Họ'}, inplace=True)

# columns_order = ['Họ', 'Đệm', 'Tên','Năm sinh', 'Giới tính', 'Nhóm máu', 'Chiều cao (cm)', 'Cân nặng (kg)']

# data2 = data2[columns_order]

# print(data2)

# data2.to_csv('data2.csv',index=False)

# Xu ly tach Ho ten cua Data1
# data1[['Họ','Đệm','Tên']] = data1['Họ tên'].apply(lambda x: pd.Series(x.split(' ', 2)))

# data1 = data1.drop(columns=['Họ tên'])

# columns_order = ['Họ', 'Đệm', 'Tên','Ngày sinh', 'Giới tính', 'Chiều cao (cm)', 'Cân nặng (kg)', 'BMI']

# data1 = data1[columns_order]

# print(data1)

# data1.to_csv('data1.csv',index=False)

# Ngay sinh - nam sinh
# data1['Ngày sinh'] = pd.to_datetime(data1['Ngày sinh'])

# data2 = pd.merge(data2, data1[['Họ', 'Đệm', 'Tên', 'Ngày sinh']], on=['Họ', 'Đệm', 'Tên'], how='left')

# data2 = data2.drop(columns=['Năm sinh'])

# columns_order = ['Họ', 'Đệm', 'Tên','Ngày sinh', 'Giới tính','Nhóm máu', 'Chiều cao (cm)', 'Cân nặng (kg)']

# data2 = data2[columns_order]

# print(data2)

# data2.to_csv('data2.csv',index=False)

#GOP BANG

data3 = pd.merge(data1,data2,how="inner" )
print("DATA 3 CONCAT")
print(data3)

data3.to_csv('data3.csv', index=False)
