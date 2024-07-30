from django.shortcuts import render
from .models import Keeper, SquadXG, SquadXGA, PlayerNpxG, PlayerNpGXG, Passing, SquadIndex

def index(request):
    return render(request, 'index.html')

def brasileirao(request):
    # Fetching top 50 rows for each required model
    keepers = Keeper.objects.all()  # No limit needed as per original requirement
    squad_xg = SquadXG.objects.all()  # No limit needed as per original requirement
    squad_xga = SquadXGA.objects.all()  # No limit needed as per original requirement
    player_npxg = PlayerNpxG.objects.all()[:50]
    player_npg_xg = PlayerNpGXG.objects.all()[:50]
    passing = Passing.objects.all()[:50]
    squad_index = SquadIndex.objects.all()  # No limit needed as per original requirement

    context = {
        'keepers': keepers,
        'squad_xg': squad_xg,
        'squad_xga': squad_xga,
        'player_npxg': player_npxg,
        'player_npg_xg': player_npg_xg,
        'passing': passing,
        'squad_index': squad_index,
    }
    
    return render(request, 'brasileirao.html', context)

def under_construction(request):
    return render(request, 'under_construction.html')
