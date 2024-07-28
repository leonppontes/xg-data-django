# brasileirao/views.py

from django.shortcuts import render

import requests
import pandas as pd

def index(request):
    return render(request, 'index.html')

def generate_dataframes():
    # The code you provided to generate the dataframes goes here
    return {
        'SI_df': SI_df,
        'squadXG_df': squadXG_df,
        'squadXGA_df': squadXGA_df,
        'playernpxG_df': playernpxG_df,
        'playernpG_xG_df': playernpG_xG_df,
        'passing_df': passing_df,
        'keeper_df': keeper_df
    }


def generate_dataframes():
    # Example URLs, update them with actual URLs
    urlKeeper = 'https://fbref.com/en/comps/24/keepersadv/Serie-A-Stats#all_stats_keeper_adv'
    urlSquad = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    urlPlayer = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    urlPassing = 'https://fbref.com/en/comps/24/passing/Serie-A-Stats'
    urlSI = 'https://fbref.com/en/comps/24/Serie-A-Stats'

    # Your existing dataframe generation code here
    keeper_df = pd.read_html(
        requests.get(urlKeeper).text.replace('<!--', '').replace('-->', '')
        , attrs={'id': 'stats_keeper_adv'}
    )[0]
    keeper_df = keeper_df[[('Unnamed: 1_level_0', 'Player'), ('Unnamed: 2_level_0', 'Nation'),
                           ('Unnamed: 4_level_0', 'Squad'), ('Unnamed: 5_level_0', 'Age'),
                           ('Unnamed: 7_level_0', '90s'), ('Expected', '/90')]]
    keeper_df.columns = ['Player', 'Nation', 'Squad', 'Age', '90s', 'PSxG-GA/90']
    keeper_df = keeper_df[~keeper_df['PSxG-GA/90'].str.contains('/90')]
    keeper_df['PSxG-GA/90'] = keeper_df['PSxG-GA/90'].astype(float)
    keeper_df = keeper_df.sort_values(by='PSxG-GA/90', ascending=False)
    keeper_df['Age'] = keeper_df['Age'].str[:-4]
    keeper_df['Nation'] = keeper_df['Nation'].str[3:]

    squad_df = pd.read_html(urlSquad)[0]
    squadXG_df = squad_df[[('Unnamed: 0_level_0', 'Squad'), ('Unnamed: 2_level_0', '90s'),
                           ('Standard', 'Gls'), ('Expected', 'xG'), ('Expected', 'G-xG')]]
    squadXG_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
    squadXG_df['xG'] = squadXG_df['xG'].astype(float)
    squadXG_df = squadXG_df.sort_values(by='xG', ascending=False)

    squad_XGA_df = pd.read_html(urlSquad)[1]
    squadXGA_df = squad_XGA_df[[('Unnamed: 0_level_0', 'Squad'), ('Unnamed: 2_level_0', '90s'),
                                ('Standard', 'Gls'), ('Expected', 'xG'), ('Expected', 'G-xG')]]
    squadXGA_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
    squadXGA_df['xG'] = squadXGA_df['xG'].astype(float)
    squadXGA_df = squadXGA_df.sort_values(by='xG', ascending=True)

    player_df = pd.read_html(
        requests.get(urlPlayer).text.replace('<!--', '').replace('-->', '')
        , attrs={'id': 'stats_shooting'}
    )[0]
    player_df = player_df[[( 'Unnamed: 1_level_0',  'Player'),
                           ('Unnamed: 2_level_0', 'Nation'),
                           ('Unnamed: 3_level_0', 'Pos'),
                           ('Unnamed: 4_level_0', 'Squad'),
                           ('Unnamed: 5_level_0', 'Age'),('Unnamed: 7_level_0', '90s'),
                           ('Standard', 'Gls'),
                           ('Expected','npxG'),('Expected', 'np:G-xG')]]
    player_df.columns=['Player', 'Nation', 'Pos', 'Squad', 'Age', '90s', 'Gls', 'npxG', 'np:G-xG']
    player_df = player_df[~player_df['npxG'].str.contains('npxG')]
    player_df['npxG'] = player_df['npxG'].astype(float)
    player_df['np:G-xG'] = player_df['np:G-xG'].astype(float)
    player_df['Age'] = player_df['Age'].str[:-4]
    player_df['Nation'] = player_df['Nation'].str[3:]
    playernpxG_df = player_df.sort_values(by='npxG', ascending=False)
    playernpG_xG_df = player_df.sort_values(by='np:G-xG', ascending=False)
    playernpxG_df = playernpxG_df.head(50)
    playernpG_xG_df = playernpG_xG_df.head(50)

    passing_df = pd.read_html(
        requests.get(urlPassing).text.replace('<!--', '').replace('-->', '')
        , attrs={'id': 'stats_passing'}
    )[0]
    passing_df = passing_df[[( 'Unnamed: 1_level_0',  'Player'),
                             ('Unnamed: 2_level_0', 'Nation'),
                             ('Unnamed: 3_level_0', 'Pos'),
                             ('Unnamed: 4_level_0', 'Squad'),
                             ('Unnamed: 5_level_0', 'Age'),('Unnamed: 7_level_0', '90s'),
                             ('Expected','xA'),('Unnamed: 30_level_0', 'PrgP')]]
    passing_df.columns=['Player', 'Nation', 'Pos', 'Squad', 'Age', '90s', 'xA', 'PrgP']
    passing_df = passing_df[~passing_df['xA'].str.contains('xA')]
    passing_df['xA'] = passing_df['xA'].astype(float)
    passing_df['Age'] = passing_df['Age'].str[:-4]
    passing_df['Nation'] = passing_df['Nation'].str[3:]
    passing_df = passing_df.sort_values(by='xA', ascending=False)
    passing_df = passing_df.head(50)

    SI_df = pd.read_html(urlSI)[0]
    SI_df = SI_df[["Squad", "MP","Pts/MP", "Last 5"]]
    def calculate_squad_moment_index(last_5_results):
        letter_values = {'W': 2.5, 'D': 1.5, 'L': 0.5}
        recent_values = [1, 2, 3, 4, 5]
        squad_moment_index = sum(letter_values[letter] * recent_values[i] for i, letter in enumerate(last_5_results.split()))
        return squad_moment_index
    SI_df['Squad Moment Index'] = SI_df['Last 5'].apply(calculate_squad_moment_index)
    HomeAway_df = pd.read_html(urlSI)[1]
    HomeAway_df = HomeAway_df[[('Unnamed: 1_level_0','Squad'), ('Home', 'xGD/90'), ('Away', 'xGD/90')]]
    HomeAway_df.columns=['Squad', 'Home xGD/90', 'Away xGD/90']
    SI_df = pd.merge(SI_df, HomeAway_df, on='Squad')
    SI_df['Squad Moment Index'] = SI_df['Squad Moment Index'].astype(float)
    SI_df = SI_df.sort_values(by='Squad Moment Index', ascending=False)

    return {
        'Squad Index': SI_df,
        'Squad xG': squadXG_df,
        'Squad xGA': squadXGA_df,
        'Player npxG': playernpxG_df,
        'Player npG-xG': playernpG_xG_df,
        'Player Assists': passing_df,
        'Keepers': keeper_df
    }

def brasileirao(request):
    dataframes = generate_dataframes()
    context = {
        'dataframes': [
            {'name': name, 'columns': df.columns, 'rows': df.values.tolist()}
            for name, df in dataframes.items()
        ]
    }
    return render(request, 'brasileirao.html', context)

def under_construction(request):
    return render(request, 'under_construction.html')

