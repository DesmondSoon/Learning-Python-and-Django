from django.contrib import admin
from django.urls import path

from todo.views import *
from players.views import *



app_name = 'players'
urlpatterns = [
    path('playeradd/', player_create_info),
    path('', player_info, name= 'player-list'),
    path('<int:player_id>/', dynamic_player_view , name = "player-view"),
    path('<int:player_id>/delete/', player_delete, name = 'player-delete'),
    # path('delete_player/',player_delete_redirect, name = "player_view_delete"),
]
