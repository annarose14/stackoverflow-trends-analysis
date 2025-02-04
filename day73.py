#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)


# In[4]:


df.head()


# In[5]:


df.tail()


# In[7]:


df.shape


# In[8]:


df.count()


# In[9]:


df.groupby("TAG").sum()


# In[10]:


df.groupby("TAG").count()


# In[11]:


df['DATE'][1]


# In[13]:


type(df['DATE'][1])


# In[14]:


print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))


# In[15]:


df.DATE=pd.to_datetime(df.DATE)
df.head()


# In[16]:


test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
test_df


# In[17]:


pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
pivoted_df


# In[18]:



reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')


# In[19]:


reshaped_df.shape


# In[20]:


reshaped_df.columns


# In[21]:


reshaped_df.head()


# In[22]:


reshaped_df.count()


# In[23]:


reshaped_df.fillna(0, inplace=True) 


# In[24]:


reshaped_df = reshaped_df.fillna(0) 


# In[25]:


reshaped_df.head()


# In[26]:


reshaped_df.isna().values.any()


# In[27]:


import matplotlib.pyplot as plt


# In[28]:


plt.plot(reshaped_df.index, reshaped_df.java)


# In[29]:


plt.figure(figsize=(16,10)) 
plt.plot(reshaped_df.index, reshaped_df.java)


# In[30]:


plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)


# In[31]:


plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python) # Tadah!


# In[32]:


for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column])


# In[33]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], 
             linewidth=3, label=reshaped_df[column].name)
 
plt.legend(fontsize=16) 


# In[34]:


# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)


# used .groupby() to explore the number of posts and entries per programming language
# 
# converted strings to Datetime objects with to_datetime() for easier plotting
# 
# reshaped our DataFrame by converting categories to columns using .pivot()
# 
# used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()
# 
# created (multiple) line charts using .plot() with a for-loop
# 
# styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
# 
# added a legend to tell apart which line is which by colour
# 
# smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.
