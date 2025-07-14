import pandas as pd

df = pd.read_excel("Data.xlsx", sheet_name=0)  # อ่านชีตแรก
df.to_csv("Data.csv", index=False)  # บันทึกเป็น CSV
