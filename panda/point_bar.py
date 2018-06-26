import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#choose col
col_point = "Custom field (Story Points)"
col_proj = "Project name"
col_ass = "Assignee"

from_file = "storypoint.csv"

def read(file):
    df = pd.read_csv(file)
    return df

def select(df):    
    l = df.loc[0:, [col_point, col_proj, col_ass]]
    f = l.groupby(col_ass).sum()
    fn = f.dropna()
    return fn.reset_index()

def draw(f):
    # choose x,y
    y = np.array(f[col_point])
    x = np.array(f[col_ass])
    #draw bar char
    plt.figure(figsize=(20,10))
    plt.bar(x,y)
    #save file
    fig = plt.gcf()
    fig.savefig('./templates/storypoint-by-person.png')
    #plt.show()

if __name__ == '__main__':
    if(len(sys.argv) > 1) :
        from_file = sys.argv[1]
    df = read(from_file)
    f = select(df)
    draw(f)
