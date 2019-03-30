{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load in file\n",
    "dat_path = os.path.join('Resources', 'budget_data.csv')\n",
    "with open(dat_path, newline='') as raw_dat:\n",
    "    raw_read = csv.DictReader(raw_dat)\n",
    "    for row in raw_read:\n",
    "        print(row['Date'], row['Profit/Losses'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read and display the CSV \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List all the columns in the table\n",
    "print(raw_dat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We only want IMDb data, so create a new table that takes the Film and all the columns relating to IMDB\n",
    "imdb_table = movie_file_pd[[\"FILM\", \"IMDB\", \"IMDB_norm\",\n",
    "                            \"IMDB_norm_round\", \"IMDB_user_vote_count\"]]\n",
    "imdb_table.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We only like good movies, so find those that scored over 7, and ignore the norm rating\n",
    "good_movies = movie_file_pd.loc[movie_file_pd[\"IMDB\"] > 7, [\n",
    "    \"FILM\", \"IMDB\", \"IMDB_user_vote_count\"]]\n",
    "good_movies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find less popular movies--i.e., those with fewer than 20K votes\n",
    "unknown_movies = good_movies.loc[good_movies[\"IMDB_user_vote_count\"] < 20000, [\n",
    "    \"FILM\", \"IMDB\", \"IMDB_user_vote_count\"]]\n",
    "unknown_movies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finally, export this file to a spread so we can keep track of out new future watch list without the index\n",
    "unknown_movies.to_excel(\"output/movieWatchlist.xlsx\", index=False)"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
