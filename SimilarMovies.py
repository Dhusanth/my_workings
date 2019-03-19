import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# ratings.head()

# pivot_table function constructing a user / movie rating matrix
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# movieRatings.head()

# extract a Series of users who rated Star Wars:
starWarsRatings = movieRatings['Star Wars (1977)']


# Corrwith function used to compute pairwise correlation of Star wars' vector with other movies
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)

similarMovies.sort_values(ascending=False)

# Size of ratings and mean ratings for movies 

import numpy as np
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()

# remove movies rated fewer than 100 people and sort topr-rated

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

# Join with original dataset - Similar movies

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.head()


df.sort_values(['similarity'], ascending=False)[:15]




