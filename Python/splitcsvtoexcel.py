import pandas as pd
import numpy as np

file_path=r"C:\Users\lJAXl\Desktop\2022Q4\yekuai136.csv"
file_path2=r"C:\Users\lJAXl\Desktop\2022Q4\yekuai136.xlsx"
df = pd.read_csv(file_path, encoding = 'utf-8')
# print(df)
row = df.shape[0]
print(row)
df1 = df[0:900000]
df2 = df[900000:1800000]
df3 = df[1800000:2700000]
df4 = df[2700000:3600000]
with pd.ExcelWriter(file_path2) as writer:
    df1.to_excel(writer, sheet_name='0~900000', index=False, header=True)
    df2.to_excel(writer, sheet_name='900000~1800000', index=False, header=True)
    df3.to_excel(writer, sheet_name='1800000~2700000', index=False, header=True)
    df4.to_excel(writer, sheet_name='2700000~3600000', index=False, header=True)