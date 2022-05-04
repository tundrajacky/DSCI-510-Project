#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import re
import numpy as np
from statistics import mean
import math
import sys
import full_dataframe as frame


# In[2]:


def data_clean(dataset):
    for i in range(dataset.shape[0]):
        dataset['Price'][i] = dataset['Price'][i].replace(',','')
        location = re.sub(r'\([^()]*\)', '', dataset['Location'][i]).rstrip()
        dataset['Location'][i] = location
        rarity = re.sub(r'\([^()]*\)', '', dataset['Rarity'][i]).rstrip()
        dataset['Rarity'][i] = rarity
        if dataset['Category'][i] == 'Fish':
            shadowsize = re.sub(r'\([^()]*\)', '', dataset['Shadow size'][i]).rstrip()
            dataset['Shadow size'][i] = shadowsize    
    return dataset

def prob(dataset):
    dataset['Price'] = pd.to_numeric(dataset['Price'])
    dataset['showup_prob'] = dataset['Rarity'].map({'Common':0.9,'Uncommon':0.5,'Rare':0.3,'Ultra-rare':0.1,'None':0})
    dataset['find_prob'] = dataset['Shadow size'].map({'6':0.95,'5':0.9,'4':0.85,'3':0.8,'2':0.75,'1':0.7,'Narrow':0.6})
    dataset['find_prob'] = dataset['find_prob'].fillna(1)
    dataset['success_prob'] = dataset['Category'].map({'Fish':0.9,'Bug':0.85})
    dataset['catch_prob'] = dataset['showup_prob'] * dataset['find_prob'] * dataset['success_prob']
    dataset['Price'] = dataset['Price'].replace(',','')
    dataset['profit'] = dataset['catch_prob'] * dataset['Price']
    dataset = dataset[dataset.catch_prob != 0]
    return dataset

def find_location(dataset,month,time):

    locationlist = []
    rank_1 = 'First'
    rank_2 = 'Second'
    rank_3 = 'Third'
    
    locationname_1 = float('nan')
    profit_1 = 0
    species_1 = 0
    rarity_1 = float('nan')
    price_1 = float('nan')
    category_1 = float('nan')
    

    locationname_2 = float('nan')
    profit_2 = 0
    species_2 = 0
    rarity_2 = float('nan')
    price_2 = float('nan')
    category_2 = float('nan')
    
    locationname_3 = float('nan')
    profit_3 = 0
    species_3 = 0
    rarity_3 = float('nan')
    price_3 = float('nan')
    category_3 = float('nan')
    
    for location in list(dataset.groupby('Location')):
        locationname = location[0]
        sub_dataset = location[1]
        profitlist = []
        maxspecies = ''
        maxrarity = ''
        maxprice = 0
        maxcategory = ''
        
        for i in sub_dataset.index.tolist():
            if month in sub_dataset['North_month'][i]:
                if time in sub_dataset['Time'][i]:
                    profitlist.append(sub_dataset['profit'][i])
                    if sub_dataset['Price'][i] > maxprice:
                        maxprice = sub_dataset['Price'][i]
                        maxspecies = sub_dataset['Name'][i]
                        maxrarity = sub_dataset['Rarity'][i]
                        maxcategory = sub_dataset['Category'][i]
        if not profitlist:
            meanprofit = 0
        else:
            meanprofit = mean(profitlist)
            
        if meanprofit > profit_1:
            locationname_1 = locationname
            profit_1 = meanprofit
            species_1 = maxspecies
            rarity_1 = maxrarity
            price_1 = maxprice
            category_1 = maxcategory
            
            
        if meanprofit > profit_2 and meanprofit < profit_1:
            locationname_2 = locationname
            profit_2 = meanprofit
            species_2 = maxspecies
            rarity_2 = maxrarity
            price_2 = maxprice
            category_2 = maxcategory
            rank_2 = 'Second'
            
        if meanprofit > profit_3 and meanprofit < profit_2:
            locationname_3 = locationname
            profit_3 = meanprofit
            species_3 = maxspecies
            rarity_3 = maxrarity
            price_3 = maxprice
            category_3 = maxcategory
            rank_3 = 'Third'
        
        locationlist = [locationname_1,rank_1,profit_1,species_1,rarity_1,price_1,category_1,locationname_2,rank_2,profit_2,species_2,rarity_2,price_2,category_2,locationname_3,rank_3,profit_3,species_3,rarity_3,price_3,category_3]
    return locationlist

def location_summary(dataset_1,dataset_2):
    for i in range(12*24):
        optimallist = find_location(dataset_1,dataset_2['Month'][i],dataset_2['Time'][i])
        for j in range(3):
            for k in range(7):
                dataset_2.iloc[i*3+j,k+2] = optimallist[j*7 + k]
    return dataset_2


# In[3]:


def default_mode():
    data_north  = frame.default_north()
    data_north_clean = data_clean(data_north)
    data_north_ready = prob(data_north_clean)
    month = np.repeat(np.repeat(range(1,13),3),24)
    time = list(np.repeat(range(0,24),3))*12
    timedict = {'Month':month,'Time':time,'Optimal Location':''*3*12*24,'Rank':''*3*12*24,'Optimal Profit':''*3*24*12,'Most Valued Species':''*3*24*12,'Rarity':''*3*24*12,'Price':''*3*24*12,'Category':''*3*24*12}
    optimallocation = pd.DataFrame(timedict)
    north = location_summary(data_north_ready,optimallocation)
    north['Optimal Profit'] = pd.to_numeric(north['Optimal Profit'])
    return north


# In[4]:


def scrape_mode():
    data_north  = frame.scrape_north()
    data_north_clean = data_clean(data_north)
    data_north_ready = prob(data_north_clean)
    month = np.repeat(np.repeat(range(1,13),3),24)
    time = list(np.repeat(range(0,24),3))*12
    timedict = {'Month':month,'Time':time,'Optimal Location':''*3*12*24,'Rank':''*3*12*24,'Optimal Profit':''*3*24*12,'Most Valued Species':''*3*24*12,'Rarity':''*3*24*12,'Price':''*3*24*12,'Category':''*3*24*12}
    optimallocation = pd.DataFrame(timedict)
    north = location_summary(data_north_ready,optimallocation)
    north['Optimal Profit'] = pd.to_numeric(north['Optimal Profit'])

    
    return north


# In[5]:


if __name__ == '__main__': #for your purpose, you can think of this line as the saying "run this chunk of code first"
    if len(sys.argv) == 1: # this is basically if you don't pass any additional arguments to the command line
        #default mode
        #print eveything or the dimensions and a sample 
        print(default_mode())
        
    elif sys.argv[1] == '--scrape': # if you pass '--scrape' to the command line
        #scrape mode
        #print a sample of the data you retrieve from your sources
        print(scrape_mode())
        

