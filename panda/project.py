import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#choose col
col_point = "Custom field (Story Points)"
col_proj = "Project name"

from_file = "project.csv"
to_file = "to_project.csv"

def run_draw():
    col_point = "Custom field (Story Points)"
    col_proj = "Project name"
    col_act = "Custom field (Actual Time)"

    from_file = "project.csv"
    to_file = "to_project.csv"

    df=pd.read_csv(from_file)
    l=df.loc[0:, [col_point, col_proj, col_act]]
    f=l.groupby(col_proj).sum()
    fn=f.dropna()
    f.plot.bar()

    #save file
    fig = plt.gcf()
    fig.savefig('./templates/project.png')

    #plt.show()

if __name__ == '__main__':
    run_draw()
