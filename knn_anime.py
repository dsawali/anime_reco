
import pandas as pd 
import numpy as np 
import sys
import matplotlib.pyplot as plt 
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

FILE_2 = 'data/rating.csv'
FILE_3 = 'data/anime_popular.csv'

def main():
    # rating = pd.read_csv(FILE_2)
    popular = pd.read_csv(FILE_3)
    
    # Adjust the one Unknown entry for One Piece
    popular['episodes'][75]='855'
    
    genre_matrix = popular['genre'].str.get_dummies(sep=',')
    type_matrix = popular['type'].str.get_dummies()
    anime_matrix = pd.concat([genre_matrix, type_matrix, popular['episodes'], popular['rating']], axis=1)

    mmscaler = MinMaxScaler()

    anime_matrix = mmscaler.fit_transform(anime_matrix)
    np.round(anime_matrix, 2)

    model = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(anime_matrix)

    distances, indices = model.kneighbors(anime_matrix)

    print(distances, indices)

if __name__ == '__main__':
    main()
