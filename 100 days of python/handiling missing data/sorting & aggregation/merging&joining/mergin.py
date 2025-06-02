# pd.merge(df1,df2,on="columns_name",how="type of join") ....how are 5 types ---inner,outer,left,right,cross
import pandas as pd
#customer dataframe
df_customers=pd.DataFrame(
    {
        'customerID':[1,2,3],
        'Name':['ramesh','kowshik','kumar']
    }
)

#order dataframe
df_orders=pd.DataFrame(
    {
        'customerID':[1,2,4],
        'orderAmount':[244,250,300]
    }
)


#merge
df_merged=pd.merge(df_customers,df_orders,on="customerID",how="right")
print('inner join')
print(df_merged)

#in output who is key is match there data will show there

#outerjoin -- value which are not match are will fill by NaN
#left-- will match with left side value and return it if not matching then will return Nan.--so name is kumar but amount is nan
# right---opposite of left will return amount but name will nan
#cross-- will combined two rows of  two dataframes

"""1df=m rows
2df=n rows
m*n row
"""