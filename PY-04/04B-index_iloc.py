# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:08:09 2017

@author: cyruslentin
"""

# import the pandas module
import pandas as pd

# create an sample dataframe 
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# create dataframe
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'deaths', 'battles', 'size', 'origin'])
print(df) 

# create index
df = df.set_index('origin')
print(df) 

df = df.set_index('company')
print(df) 

# select a column
dfp = df['size']
print(dfp)

# select two or more columns
dfp = df[['size', 'battles']]
print(dfp)
dfp = df[['size', 'battles','deaths']]
print(dfp)


# show index item 
# select every index item up to 3
df.index[0:4]
df.index[4]
df.index[4:]

# loc
# according to the pandas documentation this is a "Purely label-location based 
# indexer for selection by label". Basically, use loc for indexes with 
# meaningul label values. 

# select all rows by index label
# select all rows with the index label "Arizona" 
# row output
df.loc[:'Arizona']
# columnar output
df.loc['Arizona']

# iloc
# iloc performs integer-based access to the index, purely by position: 
# that is, if you think of the of the DataFrame as a list of values or rows
# iloc does normal 0-based list access.

# select rows by row number
# select every row up to 3
df.iloc[:2]

# select the second row
df.iloc[1:2]

# select the second and third row
df.iloc[1:3]

# select every row after the third row
df.iloc[2:]
df.iloc[:]

# select columns by column number
# select the first 2 columns
df.iloc[:,:2]
df.iloc[:,:2]
df.iloc[:,:]
df.iloc[:]


# select by conditionals (boolean)
# select rows where df.deaths is greater than 50
df[df['deaths'] > 50]

# select rows where df.deaths is greater than 500 or less than 50
df[(df['deaths'] > 500) | (df['deaths'] < 50)]

# select rows where df.deaths is greater than 500 or less than 50
df[(df['deaths'] > 500) & (df['battles'] > 5)]

# select all the regiments not named "Dragoons"
df[~(df['regiment'] == 'Dragoons')]

# ix
# ix is the combination of both .loc and .iloc. 
# ix supports both label (i.e. index label value) and positional access
# it looks first for a label and falls back to positional access if no label 
# with the given value is found. It is a handy shortcut, especially if you 
# want to do things like access your index by label but your columns by position

# select data in rows named Arizona Texas
df.ix[['Arizona', 'Texas']]

# select the third cell in the row named Arizona
df.ix['Arizona', 'deaths']

# select the third cell in the row named Arizona
df.ix['Arizona', 2]

# select the third cell down in the column named deaths
df.ix[2, 'deaths']
