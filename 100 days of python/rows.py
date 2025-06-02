#head() #tail()
#head(n) or by default 5 rows will be provide
#tail(n) or by default 5 rows will be provide
import pandas as pd
df= pd.read_excel("KUMAR.CSV")
print('Display 10 rows of first')
print(df.head())

print('Diplay 10 rows of last')
print(df.tail())
