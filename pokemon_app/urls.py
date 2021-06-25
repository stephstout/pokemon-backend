from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view(), name='pokemon_list'),
    path('pokemon/<int:pk>', views.PokemonDetails.as_view(), name="pokemon_detail")
]