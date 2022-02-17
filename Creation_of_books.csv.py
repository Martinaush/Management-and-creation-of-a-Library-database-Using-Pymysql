#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Extracting from kaggle a dataset of books

import pandas as pd

import random

url = "https://github.com/Martinaush/Data_Mining_Labs/blob/e0386ed88e7c29e039a70a51ad983bed384eb07a/books.csv?raw=true"

df = pd.read_csv(url, on_bad_lines='skip')

# Manipulating it

df = df[['bookID', 'title', 'authors']]

quantity = []

for i in range(df.shape[0]):
    
    quantity.append(random.randrange(7, 27, 4))
    
df['quantity'] = quantity

# Saving it

df.to_csv('books.csv')

