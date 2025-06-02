import pandas as pd 

data={
    "Name":['kowshik',None,'roni','prito','kok','ram','rishi'],
    "Age":[23,None,34,34,78,89,30],
    "salary":[3000,None,2000,1000,2300,5400,2233],
    "Performance":[55,None,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull())

# to find how many value are missing
print(df.isnull().sum())

