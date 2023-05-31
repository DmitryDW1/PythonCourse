import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data[''] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data.head())
# data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
# data.loc[data['whoAmI'] == 'human', 'human'] = '1'
# data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
# data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
# print(data[['robot', 'human']].head())

