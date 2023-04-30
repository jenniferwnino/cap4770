import pandas as pd
from mlxtend.frequent_patterns import fpgrowth

df = pd.read_csv('processed_data/fpgrowth.csv')

fpgrowth(df, min_support=0.6, use_colnames=True, verbose=1)

#%%
