import pandas as pd
import numpy as np

df=pd.read_csv('CaseStudy.csv')
print(df)

#1.Identify missing values in the dataset.
print(df.isnull().sum())

#2.	Fill missing Performance_Rating with the department’s average rating.
df['Performance_Rating'].fillna(df['Performance_Rating'].mean(),inplace=True)
print(df)

#3.	Replace missing Salary with the department’s median salary.
df['Salary'].fillna(df['Salary'].median(),inplace=True)
print(df)

#4.	If an employee's Projects_Completed is missing, fill it with 0.
df['Projects_Completed'] = df['Projects_Completed'].fillna(0)
print(df)

#5.	Convert Working_Hours column values like ? to NaN and fill them with the mean working hours.
df['Working_Hours'] = df['Working_Hours'].replace('?', np.nan)
# Convert Working_Hours to numeric, coercing errors to NaN
df['Working_Hours'] = pd.to_numeric(df['Working_Hours'], errors='coerce')
df['Working_Hours'].fillna(df['Working_Hours'].mean(), inplace=True)
print(df)

#6.	Fix negative values in the Age column by taking absolute values.
df['Age'] = df['Age'].abs()
print(df)

#7.	Standardize Department Names to lowercase (e.g., "HR" → "hr").
df['Department'] = df['Department'].str.lower()
print(df)

#8.	Remove duplicate records (e.g., Alice appears twice).
df.drop_duplicates(inplace=True)
print(df)

#9.	Convert Salary into integer values (if stored as float).
df['Salary'] = df['Salary'].astype(int) 
print(df)

#10. Save the cleaned dataset as cleaned_employee_data.csv.
df.to_csv('cleaned_employee_data.csv', index=False)
print(df)