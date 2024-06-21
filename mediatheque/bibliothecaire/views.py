from django.shortcuts import render
from django.http import HttpResponseRedirect
from bibliothecaire.models import Book, Dvd, Cd, BoardGame
from bibliothecaire.forms import BookForm, DvdForm, CdForm, BoardGameForm, RentedBookForm


# AFFICHAGE DE LA LISTE DES MEDIAS APP_BIBLIOTHECAIRE
def list_medias_bibliothecaire(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()

    return render(request, "bibliothecaire/list_medias_bibliothecaire.html", {
        'books': books,
        'dvds': dvds,
        'cds' : cds,
        'boardgames' : boardgames,
        })


# AFFICHAGE DE LA LISTE DES MEDIAS APP_MEMBER
def list_medias_member(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()

    return render(request, "bibliothecaire/list_medias_member.html", {
        'books': books,
        'dvds': dvds,
        'cds' : cds,
        'boardgames' : boardgames,
        })


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


# SUPPRIMER UN LIVRE
# DEUX VERSION DE REDIRECTION
# def delete_book(request, id):
#     book = Book.objects.get(pk=id)
#     book.delete()
#     books = Book.objects.all()

#     return render(request, 'bibliothecaire/list_medias_bibliothecaire.html', {'books': books})

def delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect('/bibliothecaire')

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


# SUPPRIMER UN DVD
def delete_dvd(request, id):
    dvd = Dvd.objects.get(pk=id)
    dvd.delete()
    return HttpResponseRedirect('/bibliothecaire')


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


# SUPPRIMER UN CD
def delete_cd(request, id):
    cd = Cd.objects.get(pk=id)
    cd.delete()
    return HttpResponseRedirect('/bibliothecaire')


# CREATION D'UN NOUVEAU JEU DE PLATEAU
def ajout_boardgame(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/bibliothecaire')
    
    else:
        form = BoardGameForm()
    
    return render(request,"bibliothecaire/ajout_boardgame.html", {'form': form})


# SUPPRIMER UN BOARDGAME
def delete_boardgame(request, id):
    boardgame = BoardGame.objects.get(pk=id)
    boardgame.delete()
    return HttpResponseRedirect('/bibliothecaire')


# LOUER UN BOOK
def rented_book(request):
    if request.method == 'POST':
        form = RentedBookForm(request.POST)
        if form.is_valid():
            rentedbook = form.save()
            book = rentedbook.book
            book.available = False
            book.save()

        return HttpResponseRedirect('/bibliothecaire')
    
    else:
        form = RentedBookForm()
    
    return render(request,"bibliothecaire/rented_media.html", {'form': form})