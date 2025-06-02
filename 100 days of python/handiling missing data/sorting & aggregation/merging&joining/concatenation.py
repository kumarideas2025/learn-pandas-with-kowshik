# vertically or horizontal / rows or columns
# pd.concate([df1,df2],axis=0,ignore_index=True)......true means index have to reset that data set we got
#[df1,df2]=
# axis=1 
# ignore_index=True

import pandas as pd

#region1
df_region1=pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['kowshik','kumar']
})

#region2
df_region2=pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['gopal','gupi']
})

#concatenate vertically
df_concat=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concat)