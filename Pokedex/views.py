from .models import Pokemon
from django.shortcuts import render

def lista_pokemons(request):
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, 'Pokedex/lista.html', context)