#!/usr/bin/env python
# coding: utf-8

# In[9]:


#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
 'start':'1',
 'limit':'15',
 'convert':'USD'
}
headers = {
 'Accepts': 'application/json',
 'X-CMC_PRO_API_KEY': 'f7399832-68eb-40a5-81a3-d0758df7eced',
}

session = Session()
session.headers.update(headers)

try:
 response = session.get(url, params=parameters)
 data = json.loads(response.text)
 print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
 print(e)
 
#To use this you must go into the Anaconda powershell prompt and
#use "jupyter notebook --NotebookApp.iopub_data_rate_limit 100000000"
#to increase the bitrate.


# In[2]:


type(data)


# In[22]:


import pandas as pd

#This allows you to see all the columns, not just 15
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[10]:


#This normalizes the data and makes it all pretty in a dataframe

df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now', utc=True)
df


# In[72]:


def api_runner():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'f7399832-68eb-40a5-81a3-d0758df7eced',
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
#To use this you must go into the Anaconda powershell prompt and
#use this "jupyter notebook --NotebookApp.iopub_data_rate_limit 100000000"

    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now', utc=True)
    df

    if not os.path.isfile(r'D:\Documents\Alex Projects\Python Projects\API.csv'):
        df.to_csv(r'D:\Documents\Alex Projects\Python Projects\API.csv', header='column_names')
    else:
        df.to_csv(r'D:\Documents\Alex Projects\Python Projects\API.csv', mode='a', header=False)
        
        
        


# In[77]:


import os
from time import time
from time import sleep

for i in range(333):
        api_runner()
        print('API Runner Completed')
        sleep(60) #sleep for 1 minute
exit()


# In[80]:


saved_df = pd.read_csv(r'D:\Documents\Alex Projects\Python Projects\API.csv')
saved_df


# In[97]:


df = saved_df
df


# In[81]:


df


# In[82]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[83]:


df3 = df.groupby('name',sort=False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df3



# In[84]:


df4 = df3.stack()
df4


# In[85]:


type(df4)


# In[86]:


df5 = df4.to_frame(name='values')
df5


# In[87]:


df5.count()


# In[88]:


index = pd.Index(range(90))

df6 = df5.reset_index()
df6


# In[89]:


df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[95]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'],['1h', '24h', '7d', '30d', '60d','90d'])
df7


# In[91]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[92]:


sns.catplot(x='percent_change', y='values', hue='name', data=df7, kind='point')



# In[98]:


df8 = df[['name','quote.USD.price','timestamp']]
df8 = df8.query("name == 'Bitcoin'")
df8


# In[99]:


sns.lineplot(x='timestamp',y='quote.USD.price', data = df8)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




