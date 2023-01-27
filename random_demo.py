#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:20:25 2021

@author: eshasharma
"""#
# import csv and random libraries

import csv
import pandas as pd
import random


# for random example 
from datetime import datetime

#Introduction to dataframes and csv reader    
df = pd.read_csv('largebanditdata.csv')

# Introduction to random library and seed  
from random import seed
from random import random
from random import sample
from random import choices

population = [0, 1, 2, 3] #bandit arms changed to 4 to match the input file LargeBanditData.csv
probabilities = [0.25, 0.25, 0.25, 0.25] #probabilites

for index, row in df.iterrows():
    col = choices(population, probabilities)
    colname = df.columns.values[col]
    print(index)
    print(df.loc[index])
    print(df.loc[index, colname]) # prints the value found at the chosen location
    # check if value = 1
    # if so this is a win



