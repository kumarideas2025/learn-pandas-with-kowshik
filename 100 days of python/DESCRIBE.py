#step-1 sample data frame

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
print('Descriptive Statics')
print(df.describe())

# count=is there any missing value

#mean=average of ages ,average of salary,average of performance

       #std=standard daviation
#      /                        \
# samll std                    large std
#   |                                 |
# close of average                 far from average
# (data varition is consistance)      (data variation is large)
#       |                                    |
#  example:[28,29,(30),31,32]                 [20,25,(30),35,40]


# min=minimum value
# 25%=means 1st quater of your data.
#          example:sorted edges[22,25,28,29,30,32,34,40]
#                 p1-lowest 25%[22,25]
#                 p2-next 25%[28,29]
#                 p3-next 25%[30,32]
#                 p4-highest 25%[34,40]