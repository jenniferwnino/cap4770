import pandas as pd
import numpy as np

import glob
import os

all_csvs = glob.glob(os.path.join('.', '*_us.csv'))
tri = pd.concat((pd.read_csv(f) for f in all_csvs), ignore_index=True)

tri = tri[[
    '1. YEAR',
    '2. TRIFD',
    '34. CHEMICAL'
]]

grouped = tri.groupby(by='2. TRIFD')['34. CHEMICAL'].apply(lambda x: list(np.unique(x))).to_frame()
grouped.to_pickle('tri_chemicals.pkl')
#%%
