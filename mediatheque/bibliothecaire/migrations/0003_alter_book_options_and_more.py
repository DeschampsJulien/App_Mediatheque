# Generated by Django 5.0.6 on 2024-06-18 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0002_rename_available_boardgame_sur_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Livre'},
        ),
        migrations.RenameField(
            model_name='boardgame',
            old_name='sur_place',
            new_name='available_on_site',
        ),
        migrations.CreateModel(
            name='EmpruntBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rented', models.DateField(auto_now=True)),
                ('date_restitution', models.DateField(null=True)),
                ('rented', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Loué', 'Rented'), ('Disponible', 'Available')], max_length=15)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.book')),
            ],
            options={
                'verbose_name': 'Emprunt Livre',
            },
        ),
        migrations.CreateModel(
            name='EmpruntCd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rented', models.DateField(auto_now=True)),
                ('date_restitution', models.DateField(null=True)),
                ('rented', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Loué', 'Rented'), ('Disponible', 'Available')], max_length=15)),
                ('cd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.cd')),
            ],
            options={
                'verbose_name': 'Emprunt CD',
            },
        ),
        migrations.CreateModel(
            name='EmpruntDvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rented', models.DateField(auto_now=True)),
                ('date_restitution', models.DateField(null=True)),
                ('rented', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Loué', 'Rented'), ('Disponible', 'Available')], max_length=15)),
                ('dvd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.dvd')),
            ],
            options={
                'verbose_name': 'Emprunt DVD',
            },
        ),
    ]
