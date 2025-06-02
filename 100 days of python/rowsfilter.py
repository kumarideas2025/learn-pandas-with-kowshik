import pandas as pd 

data={
    "Name":['kowshik','kumar','roni','prito','kok','ram','rishi'],
    "Age":[23,34,34,34,78,89,30],
    "salary":[3000,9000,2000,1000,2300,5400,2233],
    "Performance":[55,56,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print("sample dataframe")
print(df)

#single condition base-
high_salary=df[df['salary']>5000]
print('employee with high salary')
print(high_salary)

#multiple condition-
filtered=df[(df['Age']>30)&(df['salary']>2000)]
print('employee list age >30 + salary>2000')
print(filtered)

#if one condition is right then it will run-
filtered_or=df[(df['Age']>30)| (df['Performance']>90)]
print('employees older than 35 or greater than 90')
print(filtered_or)
