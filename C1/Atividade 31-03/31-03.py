
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


arquivo = pd.read_csv('BikeSharingDemand.csv')
df_arquivo = pd.DataFrame(arquivo)


# In[ ]:


df_arquivo.head(n=5)


# In[ ]:


df_arquivo.describe()


# In[ ]:


df_arquivo.tail(n=15)


# In[ ]:


df_arquivo.sample(n=5, random_state=1)


# In[ ]:


df_arquivo.shape


# In[ ]:


df_arquivo.info()


# In[ ]:


for column in df_arquivo:
    print(column + ":")
    print(df_arquivo[column].unique())
    print()


# In[ ]:


df_arquivo[20:31]


# In[ ]:


df_arquivo.loc[20:30]


# In[ ]:


df_arquivo.iloc[20:31]


# In[ ]:


df_arquivo['humidity']


# In[ ]:


df_arquivo.humidity


# In[ ]:


df_arquivo.loc[:, 'humidity']


# In[ ]:


df_arquivo.iloc[:, df_arquivo.columns.get_loc('humidity')]


# In[ ]:


df_arquivo['temp'].value_counts()


# In[ ]:


#13
df_arquivo[['workingday', 'humidity']]


# In[10]:


#14
df_arquivo.loc[20:30, 'workingday':'humidity']


# In[12]:


#15
df_arquivo['datetime'] = pd.to_datetime(df_arquivo['datetime'])
df_arquivo['month'] = df_arquivo['datetime'].dt.month
df_arquivo['month']


# In[13]:


#16
df_arquivo[df_arquivo['month'] == 1]


# In[20]:


#17
temp = df_arquivo.loc[: , (df_arquivo['month'] == 1) and (df_arquivo['temp'] < 14).any()]
temp


# In[22]:


#19 a
df_arquivo.groupby('season')['temp'].mean()


# In[23]:


#19 b
df_arquivo.groupby('season')['atemp'].mean()


# In[30]:


#19 c
temp = df_arquivo.groupby('season')['registered'].sum()
temp.idxmax()

