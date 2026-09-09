#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[4]:


df.shape


# In[6]:


df.head(4)


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.isnull().sum()


# In[10]:


df.drop(['Status','unnamed1'],axis =1, inplace =True)


# In[26]:


pd.isnull(df).sum()


# In[12]:


df.dropna(inplace=True)


# In[6]:


df.shape


# In[14]:


df['Amount']=df['Amount'].astype('int')


# In[16]:


df.dtypes


# In[17]:


df.columns


# # Exploratory Data Analysis
# ## Gender

# In[5]:


ax = sns.countplot(x='Gender',data=df , palette = 'pastel')
for bar in ax.containers:
    ax.bar_label(bar)


# In[12]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,hue='Amount',data = sales_gen , palette ='pastel')
plt.show()


# #### From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[20]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender',palette='muted')

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age, palette ='muted')


# #### From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# ## State

# In[26]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders',palette='muted',hue='Orders')


# In[29]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount' ,palette='muted')


# #### From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively
# ## Marital Status

# In[31]:


ax = sns.countplot(data = df, x = 'Marital_Status',palette='muted')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender',palette='muted')


# #### From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# ## Occupation

# In[37]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation',palette='muted')

for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount',palette='muted')


# #### From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# ## Product Category

# In[6]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category',palette='muted')

for bars in ax.containers:
    ax.bar_label(bars)


# In[8]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount',palette='muted')


# In[11]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders',palette='muted')


# In[7]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion:
# #### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




