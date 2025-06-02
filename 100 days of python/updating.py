import pandas as pd 

data={
    "Name":['kowshik','kumar','roni','prito','kok','ram','rishi'],
    "Age":[23,34,34,34,78,89,30],
    "salary":[3000,9000,2000,1000,2300,5400,2233],
    "Performance":[55,56,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)

# .loc[] is a method in pandas to access any cell and also can modification the cell
# df.low[row_index,"column Name"]=new value

df.loc[0,'salary']=4000
print(df)


