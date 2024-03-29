import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns

# from google.colab import drive
# drive.mount('/content/drive')


def recommend(movie_name):

    ##########
    movies = pd.read_csv("assets/movies.csv")
    ratings = pd.read_csv("assets/ratings.csv")

    final_dataset = ratings.pivot(
        index='movieId', columns='userId', values='rating')
    final_dataset.head()

    final_dataset.fillna(0, inplace=True)
    final_dataset.head()

    no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
    no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

    final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index, :]
    final_dataset = final_dataset.loc[:,
                                      no_movies_voted[no_movies_voted > 20].index]

    sample = np.array([[0, 0, 3, 0, 0], [4, 0, 0, 0, 2], [0, 0, 0, 0, 1]])
    sparsity = 1.0 - (np.count_nonzero(sample) / float(sample.size))
    csr_sample = csr_matrix(sample)
    csr_data = csr_matrix(final_dataset.values)
    final_dataset.reset_index(inplace=True)

    knn = NearestNeighbors(
        metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    knn.fit(csr_data)

    ##########

    n_movies_to_reccomend = 10
    movie_list = movies[movies['title'].str.contains(movie_name)]
    if len(movie_list):
        movie_idx = movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId']
                                  == movie_idx].index[0]
        distances, indices = knn.kneighbors(
            csr_data[movie_idx], n_neighbors=n_movies_to_reccomend+1)
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(
        ), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append(
                {'Title': movies.iloc[idx]['title'].values[0], 'Distance': val[1]})
        return recommend_frame
    else:
        return "No movies found. Please check your input"


vals = recommend("Avengers: Age of Ultron")[:5]

names = [x['Title'] for x in vals]
movies = [x[:-6].strip() for x in names]
names_new = []
for name in movies:
    if name[-5:] == ", The":
        name = "The " + name[:-5]
    names_new.append(name)
print(names_new)
