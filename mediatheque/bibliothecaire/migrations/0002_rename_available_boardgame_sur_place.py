# Generated by Django 5.0.6 on 2024-06-12 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardgame',
            old_name='available',
            new_name='sur_place',
        ),
    ]
