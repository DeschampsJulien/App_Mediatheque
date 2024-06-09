from django.db import models

class Media(models.Model):
    title = models.CharField('Titre', max_length=200)
    available = models.BooleanField('Disponible', default=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Book(Media):
    author = models.CharField( 'Auteur', max_length=150)
    
    class Meta:
        verbose_name = "livre"

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
    available = models.BooleanField('Disponible', default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Jeu de Plateau"