import pandas as pd

data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

print(data1)
print(data2)

# Đánh giá dữ liệu

print(data1.isna().sum())
print(data2.isna().sum())

print(data1[(data1['Chiều cao (cm)'] <= 0) | (data1['Cân nặng (kg)'] <= 0)])
print(data2[(data2['Chiều cao (cm)'] <= 0) | (data1['Cân nặng (kg)'] <= 0)])

# Ngay sinh - nam sinh
data1['Ngày sinh'] = pd.to_datetime(data1['Ngày sinh'])

data1['Năm sinh'] = data1['Ngày sinh'].dt.year

data2['Ngày sinh'] = pd.to_datetime(data2['Năm sinh'].astype(str) + '-01-01', format='%Y-%m-%d')

data2 = data2.merge(data1[['Ngày sinh', 'Năm sinh']], left_on='Ngày sinh', right_on='Ngày sinh', how='left')

data2 = data2.drop(columns=['Năm sinh_y','Năm sinh_x'])

columns_order = ['Họ đệm', 'Tên','Ngày sinh', 'Giới tính', 'Nhóm máu', 'Chiều cao (cm)', 'Cân nặng (kg)']

data2 = data2[columns_order]

print(data2)

data2.to_csv('data2.csv',index=False)

# Ho ten - Ho dem | Ten

data2['Tên'] = data2['Tên'].replace(r'\d+','',regex = True)

data2[['Đệm', 'Tên']] = data2['Tên'].apply(lambda x: pd.Series(x.split(' ', 1)))

data2.rename(columns={'Họ đệm': 'Họ'}, inplace=True)

columns_order = ['Họ', 'Đệm', 'Tên','Ngày sinh', 'Giới tính', 'Nhóm máu', 'Chiều cao (cm)', 'Cân nặng (kg)']

data2 = data2[columns_order]

print(data2)

data2.to_csv('data2.csv',index=False)



data1.rename(columns={'Họ tên': 'Họ'}, inplace=True)

columns_order = ['Họ', 'Đệm', 'Tên','Ngày sinh', 'Giới tính', 'Chiều cao (cm)', 'Cân nặng (kg)', 'BMI']

data1 = data1[columns_order]

print(data1)

data2.to_csv('data2.csv',index=False)





#GOP BANG
data3 = pd.concat([data1,data2], axis=1)
print("DATA 3 CONCAT")
print(data3)

data3.to_csv('data3.csv', index=False)
