from django.urls import path
from bibliothecaire import views

# NAME PERMET DE REDIRIGER DE PAGE DANS LES FICHIERS HTML
urlpatterns = [
    path('', views.list_medias_bibliothecaire, name="listmediasbibliothecaire"),
    path('ajoutbook/', views.ajout_book, name="ajoutbook"),
    path('deletebook/<int:id>/', views.delete_book, name="deletebook"),
    path('ajoutdvd/', views.ajout_dvd, name="ajoutdvd"),
    path('deletedvd/<int:id>/', views.delete_dvd, name="deletedvd"),
    path('ajoutcd/', views.ajout_cd, name="ajoutcd"),
    path('deletecd/<int:id>/', views.delete_cd, name="deletecd"),
    path('ajoutboardgame/', views.ajout_boardgame, name="ajoutboardgame"),
    path('deleteboardgame/<int:id>/', views.delete_boardgame, name="deleteboardgame"),
    path('listmediamember/', views.list_medias_member, name="listmediasmember"),
    path('rentedbook/', views.rented_book, name="rentedbook"),
]