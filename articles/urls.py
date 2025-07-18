from django.contrib import admin
from django.urls import path, include 

from . import views

app_name = "articles"

urlpatterns = [
   
    path('', views.articles_view, name='articles'),  # WICHTIG: Hier den "/" am Ende hinzufügen
    path('creer/', views.creer_view, name='creer'),
    path('<slug:slug>/', views.article_view, name='article'),  # Namensraum und Name müssen korrekt sein
    path('projets/', views.projets_liste, name='projets'),
    path('projets/ajouter/', views.ajouter_projet, name='ajouter_projet'),
]

