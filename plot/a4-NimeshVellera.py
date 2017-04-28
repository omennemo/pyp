#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:04:05 2017

@author: nimeshvellera
"""
import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt
import matplotlib.style as style

path  = "/Users/nimeshvellera/Documents/201704-NMIMS-MTech-DS-Python/plot/"
os.chdir(path)

df = pd.read_csv("cars-data.csv")

df.head()

#Dataset: cars-data.csv

#1. Distribution by mpg
style.use('ggplot')
# setting the positions and width for the bars
pos = list(range(len(df['MPG_City'])))
width = 0.33
# create a bar with pre_score data, in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['MPG_City'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=df['Make'][0])
# create a bar with mid_score data, in position pos + width,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['MPG_Highway'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=df['Make'][1])
# annotation
plt.title('Distribution of MPG')
plt.ylabel('MPG')
plt.xlabel('Make')
# set label for x ticks
plt.xticks(df.index, df.Make)
# set the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*5)
plt.ylim([0, max(df['MPG_City'] + df['MPG_Highway'])] )
# adding the legend and showing the plot
plt.legend(['MPG_City', 'MPG_Highway'], loc='upper right')
# show grid
plt.grid()
# show plot
plt.show()

print(min(df.MPG_City))
print(min(df.MPG_Highway))

print(max(df.MPG_City))
print(max(df.MPG_Highway))

bins = [0,10,20,30,40,50,60,70]
plt.hist(df.MPG_City, bins, histtype='bar', rwidth=1)
plt.title('Distribution of City Mileage')
plt.xlabel('MPG in City')
plt.ylabel('Frequency')
plt.show()

plt.hist(df.MPG_Highway, bins, histtype='bar', rwidth=1)
plt.title('Distribution of Highway Mileage')
plt.xlabel('MPG on Highway')
plt.ylabel('Frequency')
plt.show()




#2. Distribution by gears
df.head()
print(min(df.Gears))
print(max(df.Gears))


plt.hist(df.Gears)
plt.show()
#3. Distribution by gears & am
pos = list(range(len(df['MPG_City'])))
width = 0.33
# create a bar with pre_score data, in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['MPG_City'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=df['Make'][0])
# create a bar with mid_score data, in position pos + width,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['MPG_Highway'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=df['Make'][1])
# annotation
plt.title('Distribution of MPG')
plt.ylabel('MPG')
plt.xlabel('Make')
# set label for x ticks
plt.xticks(df.index, df.Make)
# set the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*5)
plt.ylim([0, max(df['MPG_City'] + df['MPG_Highway'])] )
# adding the legend and showing the plot
plt.legend(['MPG_City', 'MPG_Highway'], loc='upper right')
# show grid
plt.grid()
# show plot
plt.show()
    
#5. Relationship between weight & mpg

#6. Relationship between weight & mpg differentiated by cyl

#7. Relationship between weight & mpg differentiated by gear

#8. Boxplot gear & mpg

#9. Total TradeValue for each sector 

#10. ClosePrice for any 5 Securities

#1. HighPrice & LowPrice for any one Security

