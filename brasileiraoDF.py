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

#Squad xG Dataframes
urlSquad = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
squad_df = pd.read_html(urlSquad)[0]
squadXG_df = squad_df[[('Unnamed: 0_level_0','Squad'),('Unnamed: 2_level_0','90s'),
                    ('Standard','Gls'),('Expected','xG'),('Expected','G-xG')]]
squadXG_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
squadXG_df['xG'] = squadXG_df['xG'].astype(float)
squadXG_df = squadXG_df.sort_values(by='xG', ascending=False)
print(squadXG_df.head())

squad_XGA_df = pd.read_html(urlSquad)[1]
squadXGA_df = squad_XGA_df[[('Unnamed: 0_level_0','Squad'),('Unnamed: 2_level_0','90s'),
                    ('Standard','Gls'),('Expected','xG'),('Expected','G-xG')]]
squadXGA_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
squadXGA_df['xG'] = squadXGA_df['xG'].astype(float)
squadXGA_df = squadXGA_df.sort_values(by='xG', ascending=True)
print(squadXGA_df.head())