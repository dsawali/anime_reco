import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

FILE_1 = 'data/anime_popular.csv'
PATH_OUT = 'data/'


def splitRowELement(arr):
    return arr.split(', ')


def main():
    anime = pd.read_csv(FILE_1)

    # split genre column
    anime['genre'] = anime['genre'].apply(splitRowELement)
    genres_exploded = anime.genre.apply(
        pd.Series).stack().reset_index(
        level=1, drop=True).to_frame('genre')
    genres_grouped = genres_exploded.groupby('genre').agg({'genre': 'count'})
    genres_sorted = genres_grouped.sort_values(by='genre', ascending=False)
    


if __name__ == '__main__':
    main()
