#!/usr/bin/env python
# coding: utf-8

# ##Heading

# In[74]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[75]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[76]:


df = pd.read_csv("building_inventory.csv")


# In[12]:


df


# In[14]:


df.columns


# In[17]:


df.dtypes


# In[20]:


df.describe()


# In[22]:


df.shape


# In[24]:


(df["Year Acquired"] == 0).sum()


# In[26]:


(df["Year Constructed"] == 0).sum()


# In[28]:


(df["Square Footage"] == 0).sum()


# In[31]:


df = pd.read_csv("building_inventory.csv", na_values = {
    "Year Acquired" : 0,
    "Year Constructed" : 0,
    "Square Footage" : 0
})


# In[33]:


df.describe()


# In[43]:


plt.plot([1, 2, 3, 4], [5, 1, 2, 4], "--s")


# In[50]:


plt.plot(df["Year Constructed"], df["Year Acquired"], ".")
plt.xlabel("Year Constructed")
plt.ylabel("Year Acquired")


# In[52]:


plt.plot("Year Constructed", "Year Acquired", ".", data=df)


# In[57]:


df["Age at Acquisition"] = df["Year Acquired"] - df["Year Constructed"]


# In[59]:


df["Age at Acquisition"].describe()


# In[61]:


old_buildings = df[
    df["Age at Acquisition"] >= 0
]


# In[63]:


old_buildings.describe()


# In[68]:


plt.hist(old_buildings["Age at Acquisition"]);


# In[70]:


plt.hist(old_buildings["Age at Acquisition"], log=True);
plt.xlabel("Age at Acquisition")
plt.ylabel("Count")


# In[77]:


plt.hist(old_buildings["Age at Acquisition"], bins=64, log=True);


# In[ ]:




