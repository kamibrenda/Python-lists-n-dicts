#!/usr/bin/env python
# coding: utf-8

# ## Data Wrangling

# In[ ]:


"""Using Pandas in dropping a feature(column) and in creating a column
that calculates price column to convert it from kenyan shillings to usd.
This is a sample code and is not attached to a particular dataset"""


# Create "price_usd" column for df2 (149 pesos to the dollar in 2023)
df2["price_usd"] = df2["price_kshs"] / 149

# Drop "price_mxn" column from df2
df2.drop(columns= ["price_mxn"], inplace = True)
# Print object type, shape, and head
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
df2.head()


# In[ ]:


#To drop an observation (row) in a dataframe is done by;

"""df.dropna(inplace=True) --inplace function enables the observation's values to be completely dropped 
                            within the original dataframe itself

df.dropna() --the observation is dropped in the 'working' directory."""

#for safe practice make a copy of your dataset by with df.copy()


# In[ ]:


#make a copy of the data 
df2 = data.copy()
df2.head()


# In[ ]:


#summary
df2.describe()

