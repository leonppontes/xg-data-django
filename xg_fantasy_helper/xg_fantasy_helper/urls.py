# xg_fantasy_helper/urls.py

from django.contrib import admin
from django.urls import path
from brasileirao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('update_data/', views.index, name='update_data'),
    path('brasileirao/', views.brasileirao, name='brasileirao'),
    path('premier-league/', views.under_construction, name='premier_league'),
    path('bundesliga/', views.under_construction, name='bundesliga'),
    path('la-liga/', views.under_construction, name='la_liga'),
    path('serie-a/', views.under_construction, name='serie_a'),
]

