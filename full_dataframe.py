#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import sample
import api_crawler_3 as api
import web_scraper_3 as web
import pandas as pd
import sys


# In[2]:


def default_north():
    df_fish_north_part1 = web.get_fish_north()
    fishnamelist = df_fish_north_part1['Name'].tolist()
    df_fish_part2 = api.fish_api_df(fishnamelist)
    df_fish_north_part2 = df_fish_part2[['NameEn','Rarity','North_month','Time']]
    df_fish_north = pd.merge(left = df_fish_north_part1,right = df_fish_north_part2,left_on = 'Name',right_on = 'NameEn')
    df_fish_north = df_fish_north.drop(['NameEn'],axis = 1)
    df_fish_north['Category'] = 'Fish'
    
    df_bug_north_part1 = web.get_bug_north()
    bugnamelist = df_bug_north_part1['Name'].tolist()
    df_bug_part2 = api.bug_api_df(bugnamelist)
    df_bug_north_part2 = df_bug_part2[['NameEn','Rarity','North_month','Time']]
    df_bug_north = pd.merge(left = df_bug_north_part1,right = df_bug_north_part2,left_on = 'Name',right_on = 'NameEn')
    df_bug_north = df_bug_north.drop(['NameEn'],axis = 1)
    df_bug_north['Category'] = 'Bug'
    
    df_north = pd.concat([df_fish_north,df_bug_north], axis=0,ignore_index=True)
    df_north.to_csv('north_hemisphere_data.csv')
    return df_north


# In[3]:


def default_south():
    df_fish_south_part1 = web.get_fish_south()
    fishnamelist = df_fish_south_part1['Name'].tolist()
    df_fish_part2 = api.fish_api_df(fishnamelist)
    df_fish_south_part2 = df_fish_part2[['NameEn','Rarity','South_month','Time']]
    df_fish_south = pd.merge(left = df_fish_south_part1,right = df_fish_south_part2,left_on = 'Name',right_on = 'NameEn')
    df_fish_south = df_fish_south.drop(['NameEn'],axis = 1)
    df_fish_south['Category'] = 'Fish'
    
    df_bug_south_part1 = web.get_bug_south()
    bugnamelist = df_bug_south_part1['Name'].tolist()
    df_bug_part2 = api.bug_api_df(bugnamelist)
    df_bug_south_part2 = df_bug_part2[['NameEn','Rarity','South_month','Time']]
    df_bug_south = pd.merge(left = df_bug_south_part1,right = df_bug_south_part2,left_on = 'Name',right_on = 'NameEn')
    df_bug_south = df_bug_south.drop(['NameEn'],axis = 1)
    df_bug_south['Category'] = 'Bug'
    
    df_south = pd.concat([df_fish_south,df_bug_south], axis=0,ignore_index=True)
    df_south.to_csv('south_hemisphere_data.csv')
    return df_south


# In[4]:


def scrape_north():
    df_fish_north_part1 = web.get_fish_north()
    fishnamelist = df_fish_north_part1['Name'].tolist()
    randomfishlist = sample(fishnamelist,5)
    df_fish_part2 = api.fish_api_df(randomfishlist)
    df_fish_north_part2 = df_fish_part2[['NameEn','Rarity','North_month','Time']]
    df_fish_north = pd.merge(left = df_fish_north_part1,right = df_fish_north_part2,left_on = 'Name',right_on = 'NameEn')
    df_fish_north = df_fish_north.drop(['NameEn'],axis = 1)
    df_fish_north['Category'] = 'Fish'
    
    df_bug_north_part1 = web.get_bug_north()
    bugnamelist = df_bug_north_part1['Name'].tolist()
    randombuglist = sample(bugnamelist,5)
    df_bug_part2 = api.bug_api_df(randombuglist)
    df_bug_north_part2 = df_bug_part2[['NameEn','Rarity','North_month','Time']]
    df_bug_north = pd.merge(left = df_bug_north_part1,right = df_bug_north_part2,left_on = 'Name',right_on = 'NameEn')
    df_bug_north = df_bug_north.drop(['NameEn'],axis = 1)
    df_bug_north['Category'] = 'Bug'
    
    df_north = pd.concat([df_fish_north,df_bug_north], axis=0,ignore_index=True)
    return df_north


# In[5]:


def scrape_south():
    df_fish_south_part1 = web.get_fish_south()
    fishnamelist = df_fish_south_part1['Name'].tolist()
    randomfishlist = sample(fishnamelist,5)
    df_fish_part2 = api.fish_api_df(randomfishlist)
    df_fish_south_part2 = df_fish_part2[['NameEn','Rarity','South_month','Time']]
    df_fish_south = pd.merge(left = df_fish_south_part1,right = df_fish_south_part2,left_on = 'Name',right_on = 'NameEn')
    df_fish_south = df_fish_south.drop(['NameEn'],axis = 1)
    df_fish_south['Category'] = 'Fish'
    
    df_bug_south_part1 = web.get_bug_south()
    bugnamelist = df_bug_south_part1['Name'].tolist()
    randombuglist = sample(bugnamelist,5)
    df_bug_part2 = api.bug_api_df(randombuglist)
    df_bug_south_part2 = df_bug_part2[['NameEn','Rarity','South_month','Time']]
    df_bug_south = pd.merge(left = df_bug_south_part1,right = df_bug_south_part2,left_on = 'Name',right_on = 'NameEn')
    df_bug_south = df_bug_south.drop(['NameEn'],axis = 1)
    df_bug_south['Category'] = 'Bug'
    
    df_south = pd.concat([df_fish_south,df_bug_south], axis=0,ignore_index=True)
    return df_south


# In[8]:


if __name__ == '__main__': #for your purpose, you can think of this line as the saying "run this chunk of code first"
    if len(sys.argv) == 1: # this is basically if you don't pass any additional arguments to the command line
        #default mode
        #print eveything or the dimensions and a sample 
        print(default_north())
        print(default_south())
        
    elif sys.argv[1] == '--scrape': # if you pass '--scrape' to the command line
        #scrape mode
        #print a sample of the data you retrieve from your sources
        print(scrape_north())
        print(scrape_south())

