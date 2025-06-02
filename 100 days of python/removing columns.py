# # it will keep your data clean and free
import pandas as pd 

data={
    "Name":['kowshik','kumar','roni','prito','kok','ram','rishi'],
    "Age":[23,34,34,34,78,89,30],
    "salary":[3000,9000,2000,1000,2300,5400,2233],
    "Performance":[55,56,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)

# # df.drop(columns=["columnName"],inplace=True), for False will return a new data frame
#          |                          |
# #  remove column                  modify original data directly

# for single modify
# print('modify data')
# df.drop(columns=["Performance"],inplace=True)
# print(df)


# for multiple modify
print('modified Data')
df.drop(columns=["Performance","Age"],inplace=True)
print(df)
