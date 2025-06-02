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

print("Name(single columns return series)")
name=df['Name']
print(name)

#selecting multiple columns-
subset=df[["Name","Age"]]
print('\nsubset with name and age')
print(subset)
