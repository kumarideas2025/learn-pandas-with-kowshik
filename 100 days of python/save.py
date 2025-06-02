import pandas as pd

data={
    "Name":['koko','Tpo','kowshik'],
    "city":['banlaga','winter','dhaka'],
    "age":['20','34','90']
}

df=pd.DataFrame(data)
print(df)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)