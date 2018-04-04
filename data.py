
# coding: utf-8

# In[2]:


import csv
import pandas as pd


# In[9]:


with open('./data/cities.csv') as csvfile:
    reader = csv.reader(csvfile)
    columns = reader.__next__()
csvfile.close()

# In[11]:


print(columns)


# In[14]:


csv_df=pd.read_csv("./data/cities.csv")


# In[17]:
html_table = (csv_df.to_html(index=False))#.split('\n')
with open('./data/data_table.html', 'w') as htmlfile:
    htmlfile.writelines(html_table)
htmlfile.close()

