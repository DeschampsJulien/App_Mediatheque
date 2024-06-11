from django.shortcuts import render
from django.http import HttpResponseRedirect
from bibliothecaire.models import Book, Dvd, Cd, BoardGame
from bibliothecaire.forms import BookForm, DvdForm, CdForm, BoardGameForm


# AFFICHAGE DE LA LISTE DES MEDIAS APP_BIBLIOTHECAIRE
def list_medias(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()

    return render(request, "bibliothecaire/list_medias.html", {
        'books': books,
        'dvds': dvds,
        'cds' : cds,
        'boardgames' : boardgames
        })


# AFFICHAGE DE LA LISTE DES MEDIAS APP_MEMBER
# def list_medias(request):
#     books = Book.objects.all()
#     dvds = Dvd.objects.all()
#     cds = Cd.objects.all()
#     boardgames = BoardGame.objects.all()

#     return render(request, "member/list_medias.html", {
#         'books': books,
#         'dvds': dvds,
#         'cds' : cds,
#         'boardgames' : boardgames
#         })


# CREATION D'UN NOUVEAU LIVRE
def ajout_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BookForm()
    return render(request,"bibliothecaire/ajout_book.html", {'form': form})


# CREATION D'UN NOUVEAU DVD
def ajout_dvd(request):
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = DvdForm()
    return render(request,"bibliothecaire/ajout_dvd.html", {'form': form})


# CREATION D'UN NOUVEAU CD
def ajout_cd(request):
    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = CdForm()
    return render(request,"bibliothecaire/ajout_cd.html", {'form': form})


# CREATION D'UN NOUVEAU JEU DE PLATEAU
def ajout_boardgame(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/bibliothecaire')
    else:
        form = BoardGameForm()
    
    return render(request,"bibliothecaire/ajout_boardgame.html", {'form': form} )







