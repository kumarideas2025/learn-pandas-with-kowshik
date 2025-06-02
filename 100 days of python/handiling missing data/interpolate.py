import pandas as pd 

data={
    "Name":['kowshik','kumar','roni','prito','kok','ram','rishi'],
    "Age":[23,None,34,34,78,89,30],
    "salary":[3000,None,2000,1000,2300,5400,2233],
    "Performance":[55,None,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)

df.interpolate(method="liner",axis=0,inplace=True) #axis=0 means work on rows . #axis=1 means work on columns
