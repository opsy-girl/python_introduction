#!/usr/bin/env python
# coding: utf-8

# # This is our first class in python

# In[1]:


print("Hello world") #This is the first line of code for almost any king of programming language.


# In[2]:


#Declaring and using variable in a print statement
a=14
print("Hello participants we are welcome to the ", a , " day of free training on data analytics.")


# In[4]:


# How to install packages from the jupyter notebook
get_ipython().system('pip install pandas')


# In[22]:


# How to add a library (or package) into our current python file
import pandas as pddd


# In[6]:


# Creating series or columns or arrays in python for holding a dataset
Names = ['Ope', 'Tayo', "Micheala", "Shanon", "Josiah"]
Ages = [21,34,12,4,6]


# In[8]:


# To initialize the a dataframe
df = pddd.DataFrame()


# In[11]:


# Assign values into the series using an array
df = {'Names': ['Ope', 'Tayo', "Micheala", "Shanon", "Josiah"], 'Ages': [21,34,12,4,6]}


# In[12]:


# Display values
df


# In[14]:


# To read a file into python
df2 = pddd.read_csv('TestFile.csv')


# In[15]:


df2


# In[16]:


df2.head()


# In[17]:


df2.tail()


# In[18]:


df2.info()


# In[6]:


#Import libraries for simple visualization and numerical array
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


#create numpy arrays
x1 = np.array(["A", "B", "C", "D"])
x2 = np.array([4,6,7,3])
x3 = np.array([3, 8, 1, 10])


# In[12]:


#Create simple bar chart from matplotlib
plt.bar(x1,x2)
plt.show()


# In[13]:


#Create simple scatter chart from matplotlib
plt.scatter(x2,x3)
plt.show()


# In[15]:


#Create a dataframe from numpy arrays
import pandas as pd
nparray = np.array([['Micheal',36], ['Shanon',23], ['Debby',45], ['Ronaldo',23], ['Patience', 15]])

df = pd.DataFrame(nparray, columns = ['Names','Ages'])

print(df)


# In[ ]:




