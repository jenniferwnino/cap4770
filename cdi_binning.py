import pandas as pd
import numpy as np

cdi = pd.read_csv('CDI_with_pop_centers.csv')
cdi = cdi[[
    'YearStart',
    'YearEnd',
    'LocationAbbr',
    'LocationDesc',
    'Topic',
    'Question',
    'DataValue',
    'Latitude',
    'Longitude',
    'Centroid',
]]

topics = cdi['Topic'].value_counts().index.to_list()

topic_dfs = [cdi[cdi['Topic'] == x] for x in topics]

#%%
