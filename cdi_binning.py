import pandas as pd
import numpy as np


def bin_df(df, s='DataValue', q=5, labels=('very low', 'low', 'middle', 'high', 'very high')):
    df['Category'] = pd.qcut(x=df[s], q=q, labels=list(labels))
    return df


cdi = pd.read_csv('CDI_with_pop_centers.csv')
cdi = cdi[[
    'YearStart',
    'LocationAbbr',
    'LocationDesc',
    'Topic',
    'Question',
    'DataValue',
    'Latitude',
    'Longitude',
    'Centroid',
]]

cdi.rename(columns={'YearStart': 'Year'}, inplace=True)

topics = cdi['Topic'].value_counts().index.to_list()
bin_labels = [
    'very low',
    'low',
    'middle',
    'high',
    'very high'
]


topic_dfs = [cdi[cdi['Topic'] == x] for x in topics]

topic_dfs = [bin_df(df) for df in topic_dfs]

cdi = pd.concat(topic_dfs)
cdi = cdi[cdi['Category'].isin(['high', 'very high'])]

cdi = cdi[[
    'Year',
    'LocationAbbr',
    'LocationDesc',
    'Topic',
    'Latitude',
    'Longitude',
    'Centroid',
    'Category'
]]

grouped = cdi.groupby(by=['Year', 'LocationAbbr', 'Centroid'])['Topic'].apply(lambda x: list(np.unique(x)))
grouped.to_frame().to_csv('processed_csvs/cdi_datasets.csv')

#%%
