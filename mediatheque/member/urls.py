from django.urls import path
from member import views

urlpatterns = [
    path('', views.list_members, name="listmembers"),
    path('ajoutmember/', views.ajout_member, name="ajoutmember"),
    path('updatemember/<int:id>/', views.update_member, name="updatemember"),
    path('deletemember/<int:id>/', views.delete_member, name="deletemember"),
]