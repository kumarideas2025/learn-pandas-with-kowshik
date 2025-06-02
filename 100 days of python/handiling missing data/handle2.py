import pandas as pd 

data={
    "Name":['kowshik',None,'roni','prito','kok','ram','rishi'],
    "Age":[23,None,34,34,78,89,30],
    "salary":[3000,None,2000,1000,2300,5400,2233],
    "Performance":[55,None,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)


# fillna()
# fillna(value,inplace=True) .....so that value we here will replace with none value by default
# df.fillna(0,inplace=True)
# print(df)





#we can also fill a calculate value there ...like mean...........but have to use one default or calculate ..if try both then default value is copied in calculate value
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)

print(df)