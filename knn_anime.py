import pandas as pd 
import numpy as np 
import sys
from difflib import get_close_matches as gcm
import matplotlib.pyplot as plt 
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split


FILE_2 = 'data/rating.csv'
FILE_3 = 'data/anime_popular.csv'

popular = pd.read_csv(FILE_3)

popular.loc[popular['name']=='One Piece', 'episodes'] = 855
popular.loc[popular['name']=='Baki', 'episodes'] = 20

def get_id_from_name(name):
    return popular[popular['name']==name].index.tolist()[0]

def get_similar_anime(name):
    result = []
    for i in popular_name_list:
        if(name in i):
            result.append(i)
    return result           

def get_recommendation(name=None, id=None):
    if(id):
        for i in indices[id][1:]:
            print(popular.ix[i]['name'])
    if(name):
        found = get_id_from_name(name)
        for j in indices[found][1:]:
            print(popular.ix[j]['name'])


popular_name_list = list(popular.name.values)
popular_name_list = [x.lower() for x in popular_name_list]

genre_matrix = popular['genre'].str.get_dummies(sep=',')
type_matrix = popular['type'].str.get_dummies()
anime_matrix = pd.concat([genre_matrix, type_matrix, popular['episodes'], popular['rating']], axis=1)

mmscaler = MinMaxScaler()

anime_matrix = mmscaler.fit_transform(anime_matrix)
np.round(anime_matrix, 2)

model = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(anime_matrix)

distances, indices = model.kneighbors(anime_matrix)

print(get_recommendation('One Punch Man'))





