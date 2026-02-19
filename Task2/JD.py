#!/usr/bin/env python
# coding: utf-8

# In[2]:


years = Y = input("YEARS")
months = M = input("MONTHS: ")
days = D = input("DAYS")

Y = float(years)
M = float(months)
D = float(days)

JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5
b = f"The Julian date for your date is: {JD}"
print(b)


# In[ ]:




