"""1-how big is you dataset
2-what are the name of columns
    
shape and colums
    
shape is attribute . it will return you a tuple with 2 values
columns will returns name and could change it
"""

import pandas as pd 

data={
"Nmae":['kowshik','kumar','roni','prito','kok','ram','rishi'],
"Age":[23,34,34,34,78,89,30],
 "salary":[3000,9000,2000,1000,2300,5400,2233],
"Performance":[55,56,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print("sample dataframe")
print(df)
print(f'shape:{df.shape}')
print(f'column Names:{df.columns}')


"""(1000,20)
(5,4)
from this two will know what is the size of set with [shape]
data set structure will known from columns