#adding columns
import pandas as pd 

data={
    "Name":['kowshik','kumar','roni','prito','kok','ram','rishi'],
    "Age":[23,34,34,34,78,89,30],
    "salary":[3000,9000,2000,1000,2300,5400,2233],
    "Performance":[55,56,77,89,23,1114,44]
}
df=pd.DataFrame(data)
print(df)
#square brakcets df["column_name"]=some_Data
df["Bonus"]=df['salary']*0.1
print(df)

#another way is using insert method
# insert() --- to add any value in sepecfice position
# df.insert(loc,"column_name",some_data)
df.insert(0,"employee id",[10,20,30,40,50,60,70])
print(df)