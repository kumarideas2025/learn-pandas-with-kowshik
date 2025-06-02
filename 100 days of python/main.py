# class Math:
#     def __init__(self, num):
#         self.num = num

#     def add_to_num(self, n):
#         self.num += n

# # Create an instance of the Math class
# a = Math(5)
# print(a.num)

# # Add a number to the instance
# a.add_to_num(3)
# print(a.num)  # This will print 8

import pandas as pd
df = pd.read_excel("business-operations-survey-2023-CSV-notes.xlsx", engine='openpyxl')
print(df)
   