# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 01:09:27 2017

@author: cyruslentin
"""

import pandas as pd
import numpy as np
import os

default_path = "/Users/nimeshvellera/Documents/201704-NMIMS-MTech-DS-Python/PY-04"
os.chdir(default_path)

# read data from csv and load data in a dataframe
df = pd.read_csv('./data/Catalog.csv')
df = pd.read_csv('./data/Catalog.csv', skiprows = 3, header= None)

print(df)

df = pd.read_csv('./data/CatalogNew.csv')
df = pd.read_csv('./data/CatalogNew.csv', na_values=['.'], thousands=',')
print(df)

#==============================================================================
# # variations
# # load a csv with no headers
# df = pd.read_csv('./data/Catalog.csv', header=None)
# # load a csv while specifying column names
# df = pd.read_csv('./data/Catalog.csv', names=['Title', 'Artist', 'Country', 'Company', 'Price', 'Year'])
# # load a csv while specifying "." as missing values
# df = pd.read_csv('./data/Catalog.csv', na_values=['.'])
# # load a csv while skipping the top 3 rows
# df = pd.read_csv('./data/Catalog.csv', skiprows=3)
# # load a csv while interpreting "," in strings around numbers as thousands seperators
# df = pd.read_csv('./data/Catalog.csv', thousands=',')
# 
#==============================================================================

# see the top & bottom rows of the frame
print(df.head())
print(df.tail(3))

# display the index
print(df.index)

# display columns
print(df.columns)

# print dataframe with RowNo as index
# df[n:n]
# Note that Pandas uses zero based numbering, so 0 is the first row, 
# 1 is the second row, etc.
# 1:2 is to be read as starting 1 upto but including 2 ... prints row 1 only
print(df[1:2])
print(df[1:-1])
print(df[:])

# print dataframe column using ColName
# df['ColName']
print(df['Title'])

# print dataframe using RowNo & ColName
print(df[0:2]['Title'])

# print dataframe rows with condition
# df[ df['ColName'] condition ]
df.new = df[df['Year'] < 1990]
print(df.new)
df.new = df[df['Title'] == 'Red']
print(df.new)
df.new = df[df.Title == 'Red']
print(df.new)
df.new = df[df['Country'].isnull()]
print(df.new)
df.new = df[df['Country'].notnull()]
print(df.new)

# add new column
# assign New Column To Dataframe
# assign a new column to df called 'Age' with formula
df = df.assign(Age=2017-df['Year'])
print(df)

# create a new column called Status where the value is based on condition
# if df.age is greater than 50 
df = df.assign(Status="") 
df['Status'] = np.where(df['Age']>=30, 'GoldenOldie', 'RecentPast')
print(df)

# drop columns
# axis : {0 or ‘index’, 1 or ‘columns’}, default 0
# 0 or row/‘index’: apply function to each row
# 1 = ‘columns’: apply function to each column
df = df.drop('Company', axis=1)
df = df.drop(1, axis=0)
print(df)

# drop / delete row based on RowIndex
df.new = df.drop(df.index[2])
print(df.new)
 
# drop / delete row based on conditions
df.new = df[df.Title != 'Red']
print(df.new)


# rename column name
# rename the dataframe's column names with a new set of column names 
ColNames=['Title', 'Artist', 'Country', 'Price', 'Year', 'Age', 'Label']
df.columns = ColNames
print(df)

# rename specific column name
# rename the dataframe's column names with a new set of column names 
df=df.rename(columns = {'Label':'Status'})
print(df)

# save dataframe to csv
df.to_csv('./data/Sample.csv')