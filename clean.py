# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:14:57 2020

@author: User
"""

# Creating City_id, State_id, Year_id

import pandas as pd

file_path = 'C:\\Users\\User\\Documents\\School\\code\\CrimeETL\\'
df = pd.read_csv(file_path + '2006 - 2008 Crime in the United States (Data.gov)-CityCrime.csv')

#year dictionary
year_dict = {2006:0, 2007:1, 2008:2}
df['Year_id'] = df['Year'].map(year_dict)
df['Year_id'] = df['Year_id']+1

#City Dictionary
uniqueList = df.City.unique().tolist()
uniqueDf = pd.DataFrame(uniqueList, columns = ['City'])
city_dict = uniqueDf.City.to_dict()
city_dict_good = {y:x for x,y in city_dict.items()}
df['City_id'] = df['City'].map(city_dict_good)
df['City_id'] = df['City_id']+1

#State Dictionary
list_state = df.State.unique().tolist()
unique_state = pd.DataFrame(list_state, columns = ['State'])
dict_state = unique_state.State.to_dict()
state_dict = {y:x for x,y in dict_state.items()}
df['State_id'] = df['State'].map(state_dict)
df['State_id'] = df['State_id']+1

df.to_csv('06-08 Crime.csv', index = False)
df = pd.read_csv(file_path + '06-08 Crime.csv')