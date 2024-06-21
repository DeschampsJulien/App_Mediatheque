from django import forms
from bibliothecaire.models import Book, Dvd, Cd, BoardGame, RentedBook 


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'


class DvdForm(forms.ModelForm):
    
    class Meta:
        model = Dvd
        fields = '__all__'


class CdForm(forms.ModelForm):
    
    class Meta:
        model = Cd
        fields = '__all__'


class BoardGameForm(forms.ModelForm):
    
    class Meta:
        model = BoardGame
        fields = '__all__'



class RentedBookForm(forms.ModelForm):
    
    class Meta:
        model = RentedBook
        fields = '__all__'
    