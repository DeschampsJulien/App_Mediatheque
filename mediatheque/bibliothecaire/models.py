from django.db import models


class Media(models.Model):
    title = models.CharField('Titre', max_length=200)
    available = models.BooleanField('Disponible', default=True)

    class Meta:
        abstract = True


class Book(Media):
    author = models.CharField( 'Auteur', max_length=150)
    
    class Meta:
        verbose_name = "Livre"


class Dvd(Media):
    realizator = models.CharField( 'Réalisateur', max_length=150)
    
    class Meta:
        verbose_name = "DVD"


class Cd(Media):
    artist = models.CharField('Artiste', max_length=150)
    
    class Meta:
        verbose_name = "CD"


class BoardGame(models.Model):
    name = models.CharField('Nom', max_length=200)
    creator = models.CharField('Créateur', max_length=150)
    available_on_site = models.BooleanField('Disponible', default=True)
    
    class Meta:
        verbose_name = "Jeu de Plateau"


class Rented(models.Model):
    
    class Status(models.TextChoices):
        rented = 'Loué',
        available = 'Disponible'
    
    date_rented = models.DateField(auto_now=True)
    date_restitution = models.DateField(null=True)
    rented = models.BooleanField(default=False)
    status = models.CharField(choices=Status.choices,max_length=15)
    
    class Meta:
        abstract = True


class RentedBook(Rented):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Emprunt Livre"


class RentedDvd(Rented):
    dvd = models.OneToOneField(Dvd, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Emprunt DVD"


class RentedCd(Rented):
    cd = models.OneToOneField(Cd, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Emprunt CD"
