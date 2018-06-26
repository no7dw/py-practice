import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#choose col

from_file = "project.csv"

'''
    return dataframe
'''
def read(from_file):
    df = pd.read_csv(from_file)
    return df

def select(df):
    col_point = "Custom field (Story Points)"
    col_proj = "Project name"
    col_act = "Custom field (Actual Time)"

    l = df.loc[0:, [col_point, col_proj, col_act]]
    f = l.groupby(col_proj).sum()
    fn = f.dropna()
    return fn

def draw(fn):
    fn.plot.bar()
    #save file
    fig = plt.gcf()
    fig.savefig('./templates/project.png')
    #plt.show()

if __name__ == '__main__':
    df = read("project.csv")
    fn = select(df)
    draw(fn)
