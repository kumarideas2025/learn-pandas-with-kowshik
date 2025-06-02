#aggregation --- sum calculate, find mean, value count in entire data frame
#summarize-statistic= will minimum , maximum average of numarical number. 

# df["columns name"].mean()
# df["columns name"].sum()
# df["columns name"].min()
# df["columns name"].max()

import pandas as pd
data={
    "name":['kowshik','kumar','sarker'],
    "age":[29,24,26],
    "salary":[2000,4000,1000]
}
df=pd.DataFrame(data)
avg_salary=df['salary'].mean()
print(avg_salary)