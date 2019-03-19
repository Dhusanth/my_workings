import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# ratings.head()

# Pivot table to construct a matrix of users and the movies they rated
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()

# pandas has a built-in corr() method that will compute a correlation score for every column pair in the matrix!
# This gives us a correlation score between every pair of movies 
# (where at least one user rated both movies - otherwise NaN's will show up.)

corrMatrix = userRatings.corr()
corrMatrix.head()

# Min_periods = 100 ie fewer than 100 users rated a given movie pair

corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()

# test case - user id 0 
myRatings = userRatings.loc[0].dropna()
myRatings

# retrive similar movies that user id 0 rated

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))

# same movies came more than once

simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(10)

# filter out movies that already rated

filteredSims = simCandidates.drop(myRatings.index)
filteredSims.head(10)





