#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
# Membuat dataframe dari data yang disalin ke clipboard
df = pd.read_clipboard()

print(df)


# In[8]:


df


# In[9]:


rata_tinggi = df['TINGGI BADAN'].mean()
rata_tinggi


# In[10]:


print(df.dtypes)


# In[11]:


df['ANGKATAN'] = df['ANGKATAN'].astype(str) 


# In[12]:


print(df.dtypes)


# In[63]:


df = pd.read_csv("C:/Users/jet/Downloads/data_nama.csv")
df


# In[35]:


df = pd.read_excel("data_nama.xlsx")
df


# In[72]:


data_nama = pd.read_csv("C:/Users/jet/Downloads/data_nama.csv")
df


# In[ ]:




