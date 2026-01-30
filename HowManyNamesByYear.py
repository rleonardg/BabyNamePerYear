import pandas as pd
import numpy as np

def how_many_names_by_year(data, n, sex):
    # create a empty list to store DataFrames 
    x = []

    # filter the data by the given sex and select the relevant columns
    df = data[['name', 'year', 'count']][data['sex'] == sex]

    # transform the data to wide format
    df = df.pivot(index='name', columns='year', values='count')

    # create a list with the years for iterate it
    years = df.columns.to_numpy()

    df = df.reset_index()

    # iterate over columns and update 'x' list for names per years
    # we take the first n values
    for y in years:
        df_temp = df[['name', y]].sort_values(by=y, ascending=False).head(n)
        x.append(df_temp)

    # iterate over the x index to realize outer join
    for i in range(len(x)):
        x[i] = x[i].set_index('name')

    # concat x list to create a dataframe along columns
    df_final = pd.concat(x, axis=1)
    df_final = df_final.reset_index()

    # print(df_final)
    df_final.to_csv('baby_names_result.csv')

    


if __name__ == '__main__':
     # data = pd.read_csv("data/baby_girl_names.csv") 
     # how_many_names_by_year(data, 10, 'F')
