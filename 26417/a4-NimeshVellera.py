#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:23:32 2017

@author: nimeshvellera
"""

import numpy as np
import pandas as pd
import os

default_path = "/Users/nimeshvellera/Documents/201704-NMIMS-MTech-DS-Python/26417/"
os.chdir(default_path)

df = pd.read_csv("./weather-data.csv")

#Use scipy to find if columns are corelated
df.columns
#impute with preceeding and succeeding value
indexO = df['Ozone'].index[df['Ozone'].apply(np.isnan)]
indexS = df['Solar'].index[df['Solar'].apply(np.isnan)]
#impute with preceeding 5 and succeeding 5 values
indexW = df['Wind'].index[df['Wind'].apply(np.isnan)]
indexT = df['Temp'].index[df['Temp'].apply(np.isnan)]

for i in indexO:
    df.ix[i, 'Ozone'] = np.mean([df.ix[i-1,'Ozone'], df.ix[i+1,'Ozone']])


df['Ozone'].index[df['Ozone'].apply(np.isnan)]