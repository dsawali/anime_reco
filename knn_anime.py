
import pandas as pd 
import numpy as np 
import sys
import matplotlib.pyplot as plt 
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

FILE_2 = 'data/rating.csv'
FILE_3 = 'data/anime_popular.csv'

def main():
    rating = pd.read_csv(FILE_2)
    popular = pd.read_csv(FILE_3)
    
    popular_before_merge = popular.drop(columns=['rating'])

    rating = rating.dropna()
    rating = rating[rating['rating'] > -1]

    # rating_grouped = rating.groupby('user_id').agg({'rating':'count'}).reset_index()
    # rating_grouped = rating_grouped[rating_grouped['rating'] > 1]    

    # TODO : SELECT CERTAIN COLUMNS, AND JOIN PROPERLY, MAKE NO OVERLAPPING COLUMNS
    merged = rating.merge(popular_before_merge, on='anime_id', how='left')
    merged = merged.dropna(subset=['name'])

    print(merged)

if __name__ == '__main__':
    main()
