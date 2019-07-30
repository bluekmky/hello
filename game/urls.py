from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamemain, name="gamemain"),
    path('2/', views.game, name="gamenum"),
]
