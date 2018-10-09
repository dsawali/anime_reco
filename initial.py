import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

FILE_1 = 'data/anime.csv'
FILE_2 = 'data/rating.csv'
PATH_OUT = 'data/'

def outputTopNAnime(df, n):
    df = df[df['members'] > 500]
    top_n = df.sort_values(by='rating', ascending=False)
    top_n = top_n.head(n)
    top_n.to_csv(PATH_OUT+'anime_popular.csv', header=True, index=False)


def main():
    anime = pd.read_csv(FILE_1)
    rating = pd.read_csv(FILE_2)

    # clean ratings
    rating = rating.dropna()
    rating = rating[rating['rating'] > -1]

    # clean anime
    anime = anime[anime['genre'].str.contains('Hentai') == False]
    anime = anime[anime['type'] != 'Music']

    anime = anime[anime['members'] > 100]

    # output top 1000 most popular anime
    outputTopNAnime(anime, 100)


if __name__ == '__main__':
    main()
