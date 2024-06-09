from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book, Dvd, Cd, BoardGame
from .forms import BookForm

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

# CREATION D'UN NOUVEAU LIVRE
def ajout_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
        return HttpResponseRedirect('/list_medias')
    else:
        form = BookForm()
    return render(request,"bibliothecaire/ajout_book.html", {'form': form} )





