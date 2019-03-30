#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencie
import pandas as pd


# In[2]:


# Load in file
movie_file = "Resources/movie_scores.csv"


# In[3]:


# Read and display the CSV with Pandas
movie_file_pd = pd.read_csv(movie_file)
movie_file_pd.head()


# In[4]:


# List all the columns in the table
movie_file_pd.columns


# In[5]:


# We only want IMDb data, so create a new table that takes the Film and all the columns relating to IMDB
imdb_table = movie_file_pd[["FILM", "IMDB", "IMDB_norm",
                            "IMDB_norm_round", "IMDB_user_vote_count"]]
imdb_table.head()


# In[6]:


# We only like good movies, so find those that scored over 7, and ignore the norm rating
good_movies = movie_file_pd.loc[movie_file_pd["IMDB"] > 7, [
    "FILM", "IMDB", "IMDB_user_vote_count"]]
good_movies.head()


# In[7]:


# Find less popular movies--i.e., those with fewer than 20K votes
unknown_movies = good_movies.loc[good_movies["IMDB_user_vote_count"] < 20000, [
    "FILM", "IMDB", "IMDB_user_vote_count"]]
unknown_movies.head()


# In[8]:


# Finally, export this file to a spread so we can keep track of out new future watch list without the index
unknown_movies.to_excel("output/movieWatchlist.xlsx", index=False)

