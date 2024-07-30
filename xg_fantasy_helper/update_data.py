import os
import django
import pandas as pd
import requests
from django.conf import settings

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xg_fantasy_helper.settings')  # Replace with your project’s settings module
django.setup()

from brasileirao.models import Keeper, SquadXG, SquadXGA, PlayerNpxG, PlayerNpGXG, Passing, SquadIndex

# Function to fetch and clean data for a specific URL and table ID
def fetch_and_clean_data(url, table_id):
    response = requests.get(url)
    cleaned_html = response.text.replace('<!--', '').replace('-->', '')
    dataframe = pd.read_html(cleaned_html, attrs={'id': table_id})[0]
    return dataframe

# Fetch and update Keeper data
def update_keeper_data():
    url = 'https://fbref.com/en/comps/24/keepersadv/Serie-A-Stats#all_stats_keeper_adv'
    keeper_df = fetch_and_clean_data(url, 'stats_keeper_adv')
    keeper_df = keeper_df[[('Unnamed: 1_level_0', 'Player'),  ( 'Unnamed: 2_level_0', 'Nation'), 
                        ('Unnamed: 4_level_0', 'Squad'), ( 'Unnamed: 5_level_0', 'Age'),
                        ( 'Unnamed: 7_level_0', '90s'), ('Expected', '/90')]]
    keeper_df.columns = ['Player', 'Nation', 'Squad', 'Age', '90s', 'PSxG-GA/90']
    keeper_df = keeper_df[~keeper_df['PSxG-GA/90'].str.contains('/90')]
    keeper_df['PSxG-GA/90'] = keeper_df['PSxG-GA/90'].astype(float)
    keeper_df = keeper_df.sort_values(by='PSxG-GA/90', ascending=False)
    keeper_df['Age'] = keeper_df['Age'].str[:-4]
    keeper_df['Nation'] = keeper_df['Nation'].str[3:]

    Keeper.objects.all().delete()
    for _, row in keeper_df.iterrows():
        Keeper.objects.create(
            player=row['Player'],
            nation=row['Nation'],
            squad=row['Squad'],
            age=row['Age'],
            psxg_ga_per90=row['PSxG-GA/90'],
            nineties=row['90s']
        )

# Fetch and update SquadXG data
def update_squadxg_data():
    url = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    squad_df = pd.read_html(url)[0]
    squadXG_df = squad_df[[('Unnamed: 0_level_0','Squad'),('Unnamed: 2_level_0','90s'),
                        ('Standard','Gls'),('Expected','xG'),('Expected','G-xG')]]
    squadXG_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
    squadXG_df['xG'] = squadXG_df['xG'].astype(float)
    squadXG_df = squadXG_df.sort_values(by='xG', ascending=False)

    SquadXG.objects.all().delete()
    for _, row in squadXG_df.iterrows():
        SquadXG.objects.create(
            squad=row['Squad'],
            nineties=row['90s'],
            goals=row['Gls'],
            xg=row['xG'],
            g_xg=row['G-xG']
        )

# Fetch and update SquadXGA data
def update_squadxga_data():
    url = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    squad_XGA_df = pd.read_html(url)[1]
    squadXGA_df = squad_XGA_df[[('Unnamed: 0_level_0','Squad'),('Unnamed: 2_level_0','90s'),
                        ('Standard','Gls'),('Expected','xG'),('Expected','G-xG')]]
    squadXGA_df.columns = ['Squad', '90s', 'Gls', 'xG', 'G-xG']
    squadXGA_df['xG'] = squadXGA_df['xG'].astype(float)
    squadXGA_df = squadXGA_df.sort_values(by='xG', ascending=True)

    SquadXGA.objects.all().delete()
    for _, row in squadXGA_df.iterrows():
        SquadXGA.objects.create(
            squad=row['Squad'],
            nineties=row['90s'],
            goals=row['Gls'],
            xg=row['xG'],
            g_xg=row['G-xG']
        )

# Fetch and update PlayerNpxG data
def update_playernpxg_data():
    url = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    player_df = fetch_and_clean_data(url, 'stats_shooting')
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
    playernpxG_df = player_df.sort_values(by='npxG', ascending=False).head(100)

    PlayerNpxG.objects.all().delete()
    for _, row in playernpxG_df.iterrows():
        PlayerNpxG.objects.create(
            player=row['Player'],
            nation=row['Nation'],
            position=row['Pos'],
            squad=row['Squad'],
            age=row['Age'],
            nineties=row['90s'],
            goals=row['Gls'],
            npxg=row['npxG'],
            np_g_xg=row['np:G-xG']
        )

# Fetch and update PlayerNpGXG data
def update_playernpg_xg_data():
    url = 'https://fbref.com/en/comps/24/shooting/Serie-A-Stats'
    player_df = fetch_and_clean_data(url, 'stats_shooting')
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
    playernpG_xG_df = player_df.sort_values(by='np:G-xG', ascending=False).head(100)

    PlayerNpGXG.objects.all().delete()
    for _, row in playernpG_xG_df.iterrows():
        PlayerNpGXG.objects.create(
            player=row['Player'],
            nation=row['Nation'],
            position=row['Pos'],
            squad=row['Squad'],
            age=row['Age'],
            nineties=row['90s'],
            goals=row['Gls'],
            npxg=row['npxG'],
            np_g_xg=row['np:G-xG']
        )

# Fetch and update Passing data
def update_passing_data():
    url = 'https://fbref.com/en/comps/24/passing/Serie-A-Stats'
    passing_df = fetch_and_clean_data(url, 'stats_passing')
    passing_df = passing_df[[( 'Unnamed: 1_level_0',  'Player'),
                ('Unnamed: 2_level_0', 'Nation'),
                ('Unnamed: 3_level_0', 'Pos'),
                ('Unnamed: 4_level_0', 'Squad'),
                ('Unnamed: 5_level_0', 'Age'),('Unnamed: 7_level_0', '90s'),
                ('Expected','xA'),('Unnamed: 30_level_0', 'PrgP')]]
    passing_df.columns=['Player', 'Nation', 'Pos', 'Squad', 'Age', '90s', 'xA', 'PrgP']
    passing_df = passing_df[~passing_df['xA'].str.contains('xA')]
    passing_df['xA'] = passing_df['xA'].astype(float)
    passing_df['PrgP'] = passing_df['PrgP'].astype(float)
    passing_df['Age'] = passing_df['Age'].str[:-4]
    passing_df['Nation'] = passing_df['Nation'].str[3:]
    passing_df = passing_df.sort_values(by='xA', ascending=False).head(100)

    Passing.objects.all().delete()
    for _, row in passing_df.iterrows():
        Passing.objects.create(
            player=row['Player'],
            nation=row['Nation'],
            position=row['Pos'],
            squad=row['Squad'],
            age=row['Age'],
            nineties=row['90s'],
            xa=row['xA'],
            prgp=row['PrgP']
        )

def update_squadindex_data():
    urlSI = 'https://fbref.com/en/comps/24/Serie-A-Stats'
    
    # Fetch and clean the first table
    SI_df = pd.read_html(urlSI)[0]
    SI_df = SI_df[["Squad", "MP", "Pts/MP", "Last 5"]]

    def calculate_squad_moment_index(last_5_results):
        letter_values = {'W': 2.5, 'D': 1.5, 'L': 0.5}
        recent_values = [1, 2, 3, 4, 5]
        squad_moment_index = sum(letter_values[letter] * recent_values[i] for i, letter in enumerate(last_5_results.split()))
        return squad_moment_index

    SI_df['Squad Moment Index'] = SI_df['Last 5'].apply(calculate_squad_moment_index)

    # Fetch and clean the second table
    HomeAway_df = pd.read_html(urlSI)[1]
    HomeAway_df = HomeAway_df[[('Unnamed: 1_level_0','Squad'), ('Home', 'xGD/90'), ('Away', 'xGD/90')]]
    HomeAway_df.columns=['Squad', 'Home xGD/90', 'Away xGD/90']

    # Merge the two tables
    SI_df = pd.merge(SI_df, HomeAway_df, on='Squad')
    SI_df['Squad Moment Index'] = SI_df['Squad Moment Index'].astype(float)
    SI_df = SI_df.sort_values(by='Squad Moment Index', ascending=False)

    SquadIndex.objects.all().delete()
    for _, row in SI_df.iterrows():
        SquadIndex.objects.create(
            squad=row['Squad'],
            matches_played=row['MP'],
            points_per_match=row['Pts/MP'],
            last_5=row['Last 5'],
            squad_moment_index=row['Squad Moment Index'],
            home_xgd_per90=row['Home xGD/90'],
            away_xgd_per90=row['Away xGD/90']
        )

# Update all data
def update_all_data():
    update_keeper_data()
    update_squadxg_data()
    update_squadxga_data()
    update_playernpxg_data()
    update_playernpg_xg_data()
    update_passing_data()
    update_squadindex_data()

# Run the update function
update_all_data()
