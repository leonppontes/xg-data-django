# brasileirao/models.py
from django.db import models

class Keeper(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    psxg_ga_per90 = models.FloatField()
    nineties = models.FloatField()  # Replacing '90s' with 'nineties'

    class Meta:
        ordering = ['-psxg_ga_per90']

class SquadXG(models.Model):
    squad = models.CharField(max_length=100)
    nineties = models.FloatField()  # Replacing '90s' with 'nineties'
    goals = models.FloatField()  # Replacing 'Gls' with 'goals'
    xg = models.FloatField()
    g_xg = models.FloatField()

    class Meta:
        ordering = ['-xg']

class SquadXGA(models.Model):
    squad = models.CharField(max_length=255)
    nineties = models.FloatField()
    goals = models.FloatField()
    xg = models.FloatField()
    g_xg = models.FloatField()

    class Meta:
        ordering = ['xg']

class PlayerNpxG(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)  # Replacing 'Pos' with 'position'
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField()  # Replacing '90s' with 'nineties'
    goals = models.FloatField()  # Replacing 'Gls' with 'goals'
    npxg = models.FloatField()  # Replacing 'npxG' with 'npxg'
    np_g_xg = models.FloatField()  # Replacing 'np:G-xG' with 'np_g_xg'

    class Meta:
        ordering = ['-npxg']

class PlayerNpGXG(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)  # Replacing 'Pos' with 'position'
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField()  # Replacing '90s' with 'minutes_played'
    goals = models.FloatField()  # Replacing 'Gls' with 'goals'
    npxg = models.FloatField()  # Replacing 'npxG' with 'npxg'
    np_g_xg = models.FloatField()

    class Meta:
        ordering = ['-np_g_xg']

class Passing(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)  # Replacing 'Pos' with 'position'
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField()  # Replacing '90s' with 'nineties'
    xa = models.FloatField()  # Replacing 'xA' with 'x_a'
    prgp = models.FloatField()  # Replacing 'PrgP' with 'progressive_passes'

    class Meta:
        ordering = ['-xa']

class SquadIndex(models.Model):
    squad = models.CharField(max_length=100)
    matches_played = models.IntegerField()  # Replacing 'MP' with 'matches_played'
    points_per_match = models.FloatField()  # Replacing 'Pts/MP' with 'points_per_match'
    last_5 = models.CharField(max_length=20)  # Replacing 'Last 5' with 'last_5_results'
    squad_moment_index = models.FloatField()
    home_xgd_per90 = models.FloatField()  # Replacing 'Home xGD/90' with 'home_xgd_per90'
    away_xgd_per90 = models.FloatField()  # Replacing 'Away xGD/90' with 'away_xgd_per90'

    class Meta:
        ordering = ['-squad_moment_index']
