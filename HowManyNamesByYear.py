import pandas as pd
import numpy as np
import sys

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

    print(df_final)
    #df_final.to_csv('baby_names_result.csv')

    


if __name__ == '__main__':
    try:
        file_path, n, sex = sys.argv[1], sys.argv[2], sys.argv[3]
        if len(sys.argv) != 4:
            raise ValueError("Three arguments must be passed (file_path, n, sex)")
        if sex not in ['M', 'F']:
            raise ValueError("Argument sex has to be 'F' or 'M'")
        if not n.isdigit():
            raise TypeError("n argument has to be a number")

        data = pd.read_csv(file_path) 
        how_many_names_by_year(data, int(n), sex)
    except (ValueError, TypeError, FileNotFoundError) as e:
        print(f"{e}")
