from django.urls import path
from bibliothecaire import views


urlpatterns = [
    path('', views.list_medias_bibliothecaire, name="listmediasbibliothecaire"),
    path('ajoutbook/', views.ajout_book, name="ajoutbook"),
    path('ajoutdvd/', views.ajout_dvd, name="ajoutdvd"),
    path('ajoutcd/', views.ajout_cd, name="ajoutcd"),
    path('ajoutboardgame/', views.ajout_boardgame, name="ajoutboardgame"),
    path('member/', views.list_medias_member, name="listmediasmember"),
]