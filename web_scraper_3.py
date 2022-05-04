#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys


# In[2]:


def get_tables_fish(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    tables = soup.findAll('table',attrs = {'class':'roundy sortable'})
    return tables


# In[3]:


def get_tables_bug(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    tables = soup.findAll('table')
    return tables


# In[4]:


def get_content(table):
    body = table.findAll('tr')
    head = body[0]
    row = body[1:]
    headlist = []
    for item in head.findAll('th'):
        item = item.text.rstrip('\n')
        headlist.append(item)
    rowlist = []
    for i in range(len(row)):
        eachrow = []
        for item in row[i].findAll('td'):
            item = item.text.rstrip('\n')
            eachrow.append(item)
        rowlist.append(eachrow)
    return headlist,rowlist


# In[5]:


def table_to_dataframe(headlist,rowlist):
    fish_df_1 = pd.DataFrame(data = rowlist,columns = headlist)
    return(fish_df_1)


# In[6]:


def get_fish_north():
    url = 'https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)'
    tables = get_tables_fish(url)
    headlist,rowlist = get_content(tables[0])
    fish_df_1_north = table_to_dataframe(headlist,rowlist)
    fish_north_final = fish_df_1_north[['Name','Price','Location','Shadow size']]
    return fish_north_final


# In[7]:


def get_fish_south():
    url = 'https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)'
    tables = get_tables_fish(url)
    headlist,rowlist = get_content(tables[1])
    fish_df_1_south = table_to_dataframe(headlist,rowlist)
    fish_south_final = fish_df_1_south[['Name','Price','Location','Shadow size']]
    return fish_south_final


# In[8]:


def get_bug_north():
    url = 'https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)'
    tables = get_tables_bug(url)
    headlist,rowlist = get_content(tables[2])
    bug_df_1_north = table_to_dataframe(headlist,rowlist)
    bug_north_final = bug_df_1_north[['Name','Price','Location']]
    return bug_north_final


# In[9]:


def get_bug_south():
    url = 'https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)'
    tables = get_tables_bug(url)
    headlist,rowlist = get_content(tables[3].find('table'))
    bug_df_1_south = table_to_dataframe(headlist,rowlist)
    bug_south_final = bug_df_1_south[['Name','Price','Location']]
    return bug_south_final

