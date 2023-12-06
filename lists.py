#!/usr/bin/env python
# coding: utf-8

# # Python and lists

# In[1]:


"""House list is from a tabular dataset where features = (columns) and observations = (rows).
In this list 115910.26 = Price, 128 = square metres and 4 = No. of rooms"""

house_list = [115910.26, 128, 4]

#To find the price per metres squared Price/metres squared
house_price_m2 = house_list[0] / house_list[1]

house_price_m2


# In[2]:


#To add the new column house_price_m2 - append the list
house_list.append(house_price_m2)

#To create a nested list to store more than 1 dataset
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]
print(house_list, houses_nested_list)



# In[3]:


# Create for loop to iterate through `houses_nested_list`
for house in houses_nested_list:
    Price_m2 = house[0] / house[1]
    house.append(Price_m2)
houses_nested_list


# In[4]:


#Working with for loops within a list.
price_usd = [97919.38, 300511.20, 293758.14, 540244.86]
for x in price_usd:
    print(x)


# # Python and Dictonaries

# ### Values

# In[5]:


"""Creating a dictionary
key-value pair is how data is stored in the dictionary. In this case, the keys are Price_usd and value is '121555.09' and so on."""

Bogota = {
    'Price_usd' : 121555.09,
    "area_m2" : 82,
    "property_type" : "house",
}
print(Bogota)

#Accessing a value in the dictionary using the key 
x = Bogota["area_m2"]
print(x)

#To get the value in the dictionary
x = Bogota.get("area_m2")


# ### Keys

# In[6]:


#To list keys in a dictionary
Bogota.keys()

#To store the keys in a list(stores mutiple itams in a single variable)
list(Bogota.keys())

#Listing the keys in a dictionary without using a list
for x in Bogota.keys():
    print(x)


# ### A list of dictionaries with basic mean calculation

# In[7]:


"""Putting a a dictionary with mutiple variables in a list and declaring the variables. The calculation to be done is all executed within the observation(row)."""

house_obs_dict = [
    {
        "price_in_usd": 115910.26,
        "surface_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_in_usd": 48718.17,
        "surface_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_in_usd": 28977.56,
        "surface_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_in_usd": 36932.27,
        "surface_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_in_usd": 83903.51,
        "surface_in_m2": 111,
        "rooms": 3,
    },
]

print(house_obs_dict)

"""Calculating the price per squared metres using dictionaries. This is in reference with the housing data we had earlier used in the lists"""
house_dict = {
    "price_in_usd": 115910.26,
    "surface_in_m2": 128,
    "rooms": 4,
}

#Calculating the price per metres squared for the house and adding it to the dictionary with its Key-Value pair
house_dict["price_m2"] = house_dict["price_in_usd"] / house_dict["surface_in_m2"]
print(house_dict)



# #### Mean calculations on observations(rows) and features(columns)

# In[8]:


#OBSERVATION (ROW)
"""Calculate the price per squared metres for each observation(rows) """
for house in house_obs_dict:
    house["price_per_m2"] = house["price_in_usd"] / house["surface_in_m2"]
print(house_obs_dict)


#FEATURES (COLUMNS) 
"""Calculting the mean price of houses within the feature(columns). This is method 1 which is typically longer and involves lists but is still effective. """
#create an empty list for prices
house_prices = []
#iterate through all the features and add their prices to the list
for house in house_obs_dict:
    house_prices.append(house["price_in_usd"])
print(house_prices)

mean_price = sum(house_prices) / len(house_prices)
print(mean_price)

"""This is method 2 which involves creating a dictionary in a list for easier manpulation and organisation of data."""
#creating a dictionary in a list
houses_feat = {
    "price_in_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}
#Calculate the total mean prices of the houses.
houses_feat["total_mean_price"] = sum(houses_feat["price_in_usd"]) / len(houses_feat["surface_in_m2"])
print(houses_feat)


# In[9]:


"""Calculating the price per metre squared within the feature(column) with introduction of the calculated feature as part of the features."""

#declare variables area and price to the values within the feature 
price = houses_feat["price_in_usd"]
area = houses_feat["surface_in_m2"]

total_price_m2 = []



for p, a in zip(price, area):    
    price_m2 = p / a
    total_price_m2.append(price_m2)

houses_feat["total_price_m2"] = total_price_m2

houses_feat



# In[10]:


print(list(total_price_m2))


# ## Dispalying the information in a dataframe using pandas

# In[11]:


import pandas as pd

df_house_prices = pd.DataFrame(houses_feat)

df_house_prices


# In[12]:


"""To drop a column price_m2
df_house_prices.drop('price_m2', axis=1, inplace=True)"""


# In[13]:


df_house_prices


# In[14]:


df_house_prices.drop('total_mean_price', axis=1, inplace=True)


# In[15]:


df_house_prices


# In[ ]:




