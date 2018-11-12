import pandas as pd

df = pd.DataFrame({'rx': pd.Series([5,6,8,9,12,15], index = ['1','2','3','4','5','6']) , 
		  'px': pd.Series([.15,.2,.3,.2,.1,.05],index = ['1','2','3','4','5','6'] ) } )
df['px.rx'] = df['rx']*df['px']
exp_return = df['px.rx'].sum()
print(df)
print('Expected Return is:', exp_return, '%')
