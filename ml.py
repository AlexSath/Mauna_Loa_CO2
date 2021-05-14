##This file contains functions that plots mauna_loa carbon dioxide data
import pandas as pd
import matplotlib.pyplot as plt

def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    df = pd.read_csv(filename)
    df['Years_Since'] = df['year'] - df['year'][0]
    df = df[['Years_Since', 'C02']]
    return df

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    plt.plot(df.Years_Since, df.C02)
    plt.xlabel("Years Since 1958")
    plt.ylabel("CO2 Levels")
    plt.title("CO2 Levels vs. Years Since CO2 Concentration Observations Began")
    
    