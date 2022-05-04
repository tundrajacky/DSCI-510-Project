#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import sys


# In[2]:


host = 'https://acnhapi.com/v1a/'
fishquery = 'fish/'
bugquery = 'bugs/'
apikey = ''


# In[3]:


def get_api_fish(fish):
    try:
        fish_str = fish.lower().replace(' ','_')
        url = host+fishquery+fish_str+apikey
        fish_json = requests.get(url).json()
        rarity = fish_json['availability']['rarity']
        north_month = fish_json['availability']['month-array-northern']
        south_month = fish_json['availability']['month-array-southern']
        time = fish_json['availability']['time-array']
        fish_apilist = [fish,rarity,north_month,south_month,time]
        return fish_apilist
    except:
        return [fish,'None','None','None','None']


# In[4]:


def fish_api_df(fishlist):
    fish_dict = {'NameEn':[],'Rarity':[],'North_month':[],'South_month':[],'Time':[]}
    for fish in fishlist:
        fish_apiinfo = get_api_fish(fish)
        fish_dict['NameEn'].append(fish_apiinfo[0])
        fish_dict['Rarity'].append(fish_apiinfo[1])
        fish_dict['North_month'].append(fish_apiinfo[2])
        fish_dict['South_month'].append(fish_apiinfo[3])
        fish_dict['Time'].append(fish_apiinfo[4])
    fish_df_2 = pd.DataFrame(fish_dict)
    return (fish_df_2)


# In[5]:


def get_api_bug(bug):
    try:
        bug_str = bug.lower().replace(' ','_')
        url = host+bugquery+bug_str+apikey
        bug_json = requests.get(url).json()
        rarity = bug_json['availability']['rarity']
        north_month = bug_json['availability']['month-array-northern']
        south_month = bug_json['availability']['month-array-southern']
        time = bug_json['availability']['time-array']
        bug_apilist = [bug,rarity,north_month,south_month,time]
        return bug_apilist
    except:
        return [bug,'None','None','None','None']


# In[6]:


def bug_api_df(buglist):
    bug_dict = {'NameEn':[],'Rarity':[],'North_month':[],'South_month':[],'Time':[]}
    for bug in buglist:
        bug_apiinfo = get_api_bug(bug)
        bug_dict['NameEn'].append(bug_apiinfo[0])
        bug_dict['Rarity'].append(bug_apiinfo[1])
        bug_dict['North_month'].append(bug_apiinfo[2])
        bug_dict['South_month'].append(bug_apiinfo[3])
        bug_dict['Time'].append(bug_apiinfo[4])
    bug_df_2 = pd.DataFrame(bug_dict)
    return (bug_df_2)

