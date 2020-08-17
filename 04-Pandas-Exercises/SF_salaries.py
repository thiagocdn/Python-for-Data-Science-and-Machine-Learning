import pandas as pd

sal = pd.read_csv('./04-Pandas-Exercises/assets/Salaries.csv')

print(sal, '\n')
print(sal.info(), '\n')
print(sal['BasePay'].mean(), '\n')
print(sal['OvertimePay'].max(), '\n')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'], '\n')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'], '\n')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()], '\n')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()], '\n')
print(sal.groupby('Year').mean()['BasePay'], '\n')
print(sal['JobTitle'].nunique(), '\n')
print(sal['JobTitle'].value_counts().head(), '\n')

sal_2013 = sal[sal['Year'] == 2013]

print(sum(sal_2013['JobTitle'].value_counts() == 1), '\n')


def check_chief(title):
    if 'chief' in title.lower():
        return True
    return False


print(sum(sal['JobTitle'].apply(lambda x: check_chief(x))), '\n')

sal['title_length'] = sal['JobTitle'].apply(len)
print(sal[['title_length', 'TotalPayBenefits']].corr())
