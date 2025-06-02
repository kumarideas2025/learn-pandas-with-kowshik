import pandas as pd
data={
    "name":['kowshik','kumar','sarker','roy','rishi'],
    "age":[29,28,26,29,26],
    "salary":[2000,4000,1000,4500,1200]
}
df=pd.DataFrame(data)
grouped=df.groupby("age")["salary"].sum()
print(grouped)


# df.groupby("age")
# age=28>(4000)
# age=30>(4500)
# means it will make two same age salary total sum 
