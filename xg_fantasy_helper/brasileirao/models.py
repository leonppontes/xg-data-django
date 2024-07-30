# brasileirao/models.py
from django.db import models

class Keeper(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    psxg_ga_per90 = models.FloatField()
    nineties = models.FloatField()  

    class Meta:
        ordering = ['-psxg_ga_per90']

class SquadXG(models.Model):
    squad = models.CharField(max_length=100)
    nineties = models.FloatField()
    goals = models.IntegerField() 
    xg = models.FloatField()
    g_xg = models.FloatField()

    class Meta:
        ordering = ['-xg']

class SquadXGA(models.Model):
    squad = models.CharField(max_length=255)
    nineties = models.FloatField()
    goals = models.IntegerField()
    xg = models.FloatField()
    g_xg = models.FloatField()

    class Meta:
        ordering = ['xg']

class PlayerNpxG(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10) 
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField() 
    goals = models.IntegerField() 
    npxg = models.FloatField()  
    np_g_xg = models.FloatField()  

    class Meta:
        ordering = ['-npxg']

class PlayerNpGXG(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField()  
    goals = models.IntegerField()  
    npxg = models.FloatField()  
    np_g_xg = models.FloatField()

    class Meta:
        ordering = ['-np_g_xg']

class Passing(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)  
    squad = models.CharField(max_length=100)
    age = models.IntegerField()
    nineties = models.FloatField()  
    xa = models.FloatField()  
    prgp = models.IntegerField()

    class Meta:
        ordering = ['-xa']

class SquadIndex(models.Model):
    squad = models.CharField(max_length=100)
    matches_played = models.IntegerField()  
    points_per_match = models.FloatField()  
    last_5 = models.CharField(max_length=20)  
    squad_moment_index = models.FloatField()
    home_xgd_per90 = models.FloatField()  
    away_xgd_per90 = models.FloatField()  

    class Meta:
        ordering = ['-squad_moment_index']
