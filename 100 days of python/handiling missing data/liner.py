import pandas as pd 
data={
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print('Before interpolation')
print(df)

df['value']=df['value'].interpolate(method="linear")
print('After interpolation')
print(df)

 
"""_1-time series data
2-numeric data with trends
3-avoid dropping rows_
4-catagorial data cannot work like name or id
"""