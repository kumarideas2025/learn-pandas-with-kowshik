# how to drop missing value
# so  we remove that missing value row or columns

# method
# dropna()

# df.dropna(axis=0,inplace=True)....................axis=0 means drop rows with missing columns(remove rows missing value),axis=1 means drop columns with missing rows(remove columns missing value)

import pandas as pd 

data={
    "Name":['kowshik',None,'roni','prito','kok','ram','rishi'],
    "Age":[23,None,34,34,78,89,30],
    "salary":[3000,None,2000,1000,2300,5400,2233],
    "Performance":[55,None,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)
df.dropna(inplace=True)
print(df)

# output: we could see that none value is total remove with it is columns
