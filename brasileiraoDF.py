import requests
import pandas as pd

#Keepers Dataframe
urlKeeper= 'https://fbref.com/en/comps/24/keepersadv/Serie-A-Stats#all_stats_keeper_adv'
keeper_df = pd.read_html(
    requests.get(urlKeeper).text.replace('<!--','').replace('-->','')
    ,attrs={'id':'stats_keeper_adv'}
)[0]
keeper_df = keeper_df[[('Unnamed: 1_level_0', 'Player'),  ( 'Unnamed: 2_level_0', 'Nation'), 
                    ('Unnamed: 4_level_0', 'Squad'), ( 'Unnamed: 5_level_0', 'Age'),
                    ( 'Unnamed: 7_level_0', '90s'), ('Expected', '/90')]]
keeper_df.columns = ['Player', 'Nation', 'Squad', 'Age', '90s', 'PSxG-GA/90']
keeper_df = keeper_df[~keeper_df['PSxG-GA/90'].str.contains('/90')]
keeper_df['PSxG-GA/90'] = keeper_df['PSxG-GA/90'].astype(float)
keeper_df = keeper_df.sort_values(by='PSxG-GA/90', ascending=False)
keeper_df['Age'] = keeper_df['Age'].str[:-4]
keeper_df['Nation'] = keeper_df['Nation'].str[3:]
print(keeper_df.head())
