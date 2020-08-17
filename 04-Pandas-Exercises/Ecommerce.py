import pandas as pd


ecom = pd.read_csv('./04-Pandas-Exercises/assets/Ecommerce Purchases')
print(ecom.head(5), '\n')

print(ecom.info(), '\n')

print(ecom['Purchase Price'].mean(), '\n')
print(ecom['Purchase Price'].max(), '\n')
print(ecom['Purchase Price'].min(), '\n')

print(sum(ecom['Language'] == 'en'), '\n')
print(sum(ecom['Job'] == 'Lawyer'), '\n')

print(ecom['AM or PM'].value_counts(), '\n')

print(ecom['Job'].value_counts().head(5), '\n')

print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'], '\n')

print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'], '\n')

print(ecom[(ecom['CC Provider'] == 'American Express')
           & (ecom['Purchase Price'] > 95)].count(), '\n')

print(sum(ecom['CC Exp Date'].apply(lambda x: x.split('/')[1]) == '25'))

print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
