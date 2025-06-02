#sorting data
#sorting data in one columns: method
# sort_values()

# df.sort_values(by="column Name",True/False,inplace=True).....true=asendding order/ false=desending order

import pandas as pd
data={
    "name":['kowshik','kumar','sarker'],
    "age":[29,24,26],
    "salary":[2000,4000,1000]
}
df=pd.DataFrame(data)
df.sort_values(by="age",ascending=False, inplace=True)
print('sorted age by descending')
print(df)

