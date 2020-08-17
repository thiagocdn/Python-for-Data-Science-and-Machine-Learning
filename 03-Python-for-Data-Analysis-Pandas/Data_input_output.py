from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('./03-Python-for-Data-Analysis-Pandas/assets/example')
print('Our read df:\n', df, '\n')

df.to_csv('./03-Python-for-Data-Analysis-Pandas/assets/my_output', index=False)
print('Reading our saved file:\n', pd.read_csv(
    './03-Python-for-Data-Analysis-Pandas/assets/my_output'), '\n')

df_excel = pd.read_excel(
    './03-Python-for-Data-Analysis-Pandas/assets/Excel_Sample.xlsx', sheet_name='Sheet1', index_col=0)
print('Our read excel file:\n', df_excel, '\n')

# Saving file to excel
df.to_excel(
    './03-Python-for-Data-Analysis-Pandas/assets/Excel_Sample_saved.xlsx', sheet_name='Test')

# data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

# print(data[0])
# print(data[0].head())


engine = create_engine('sqlite:///:memory:')

df.to_sql('sql_output', engine)

sqldf = pd.read_sql('sql_output', con=engine)

print('Out sqldf:\n', sqldf, '\n')
