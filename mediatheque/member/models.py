from django.db import models


class Member(models.Model):
    first_name = models.CharField('prènom', max_length=50)
    last_name = models.CharField('nom', max_length=50)
    email = models.EmailField('Mail', max_length=100)
    
    class Meta:
        verbose_name = "member"

