from django.urls import path
from member import views

urlpatterns = [
    path('', views.list_members, name="listmembers"),
    path('ajoutmember/', views.ajout_member, name="ajoutmember"),
    # path('listmedias/', views.listmedias, name="listmedias"),
    # path('ajoutmedia/', views.ajoutmedia, name="ajoutmedia"),
]