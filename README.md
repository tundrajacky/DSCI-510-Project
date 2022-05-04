# DSCI-510-Project
For my final project, I would like to analyze the most profitable way to play the game “Animal Crossing”. Basically, the easiest way to make money in this game is to catch and sell animals. In this project, two main kinds of species will be analyzed, Fish and Bugs. It should be noted that all animals will show up in their routine time and time in this game is corresponding to one in the real world.
The first two datasets I found for web scraping were:
https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons) https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)
These two datasets include all fish and bugs the game has. We could get the basic information from them such as name, price, location, and image.
For the data achieved from external public API, the host will be https://acnhapi.com/v1a/ We could get the rarity of all species which we may use as a probability of show-up rate.
The purpose of this project is that given a specific time, the result will show one or several locations to go to by finding the largest expect profit of selling species which could be found at each location.

To access the full code, three py files and two csv files are needed. The "api_crawler_3.py" and "web_scraper_3.py" are files that collect data from websites and API. The file "full_dataframe.py" is used to merge the full dataset. Also, "full_dataframe.py" has two modes for command line calling, the default mode will print the whole dataset and scrape mode will print random ten lines of full dataset. "north_hemisphere_data.csv" and "south_hemisphere_data.csv" are generated from "full_dataframe.py" and they are the full datasets for north and south hemisphere. 

The "full_analyze.py" generates the final dataframe and plots. It also got two modes, the default mode will show full dataset and full plots and the scrape mode will show the results from random ten lines get from the scrape mode of "full_dataframe.py".

The libraries needed are pandas, seaborn, re, numpy, statistics, math, random, BeautifulSoup, requests and sys.

There is also a pdf file including all analyzing process and explanations.
