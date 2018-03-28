import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#choose col
col_point = "Custom field (Story Points)"
col_proj = "Project name"
col_ass = "Assignee"

from_file = "storypoint.csv"
to_file = "new_storypoints.csv"

df=pd.read_csv(from_file)
l=df.loc[0:, [col_point, col_proj, col_ass]]
f=l.groupby(col_ass).sum()
fn=f.dropna()

fn.to_csv(to_file)
pd.read_csv(to_file)
f=pd.read_csv(to_file)

# choose x,y
y=np.array(f[col_point])
x=np.array(f[col_ass])
#draw bar char
plt.figure(figsize=(20,10))
plt.bar(x,y)
plt.show()
#save file
fig = plt.gcf()
fig.savefig('result.png')

