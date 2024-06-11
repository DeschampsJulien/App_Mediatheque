from django.shortcuts import render

# AFFICHAGE PAGE D'ACCUEIL
def home(request):
    return render(request, 'mediatheque/home.html')