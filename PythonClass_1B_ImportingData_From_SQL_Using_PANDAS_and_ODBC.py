#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Install the necessary libraries
get_ipython().system('pip install pyodbc')
get_ipython().system('pip install pandas')


# In[7]:


#Import the library into your working file
import pandas as pd
import pyodbc as py


# In[8]:


#Create a python connection to Microsoft SQL DB. Watch the training video on how to create an Data source network (DSN) connection
#Replace the DSN connection name below. Please note that this connection type is for Windows authentication type on MS SQL
conn = py.connect('DSN={DSN_Connection_Name};Trusted_Connection=yes;')


# In[31]:


#Example 1: Read data from Customers table in SQL. Write SQL script to extract the data from MS SQL into Python
cursor = conn.cursor() 

finalTable = []

cursor.execute('SELECT * FROM [dbo].[Customers]') 


# In[29]:


#Read the data items row by row into a dataframe using a loop function

for row in cursor:
    
   finalTable.append({
        '_CustomerId': row[0],
'CustomerNames': row[1]
        }) 

final = pd.DataFrame.from_dict(finalTable) 


# In[34]:


#Check data
final.head()


# In[31]:


#Example 2: Read from another table in the same database. Write SQL script to extract the data from MS SQL into Python
cursor = conn.cursor() 

finalTable = []

cursor.execute('SELECT * FROM [dbo].[Sales_Orders]') 


# In[32]:


#Read the data items row by row into a dataframe using a loop function

for row in cursor:
    
   finalTable.append({
       'OrderNumber': row[0],
'SalesChannel': row[1],
'WarehouseCode': row[2],
'ProcuredDate': row[3],
'OrderDate': row[4],
'ShipDate': row[5],
'DeliveryDate': row[6],
'CurrencyCode': row[7],
'_SalesTeamID': row[8],
'_CustomerID': row[9],
'_StoreID': row[10],
'_ProductID': row[11],
'OrderQuantity': row[12],
'DiscountApplied': row[13],
'UnitPrice': row[14],
'UnitCost': row[15] 
        }) 

final = pd.DataFrame.from_dict(finalTable) 


# In[33]:


#Check data
final.info()


# In[ ]:




