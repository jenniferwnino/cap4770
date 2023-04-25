import pandas as pd

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

topic_dfs = [cdi[cdi['Topic'] == x] for x in topics]
for df in topic_dfs:
    bin_labels = [
        'very low',
        'low',
        'middle',
        'high',
        'very high'
    ]
    name = pd.unique(df['Topic'])[0]
    df['Category'] = pd.qcut(x=df['DataValue'], q=5, labels=bin_labels)
    df.to_csv(f'./processed_csvs/{name.lower()}.csv', index=False)
#%%
