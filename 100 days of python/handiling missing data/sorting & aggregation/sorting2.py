# sorting multiple columns:
# df.sort_values(by=["age","salary"],ascending=True,inplace=True)


import pandas as pd
data={
    "name":['kowshik','kumar','sarker'],
    "age":[29,24,26],
    "salary":[2000,4000,1000]
}
df=pd.DataFrame(data)
df.sort_values(by=["age","salary"],ascending=[True,True], inplace=True) #if only set one ascending valu that will not modify t all
print('sorted age by descending')
print(df)
