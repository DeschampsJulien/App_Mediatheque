# Generated by Django 5.0.6 on 2024-06-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0003_alter_book_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmpruntBook',
            new_name='RentedBook',
        ),
        migrations.RenameModel(
            old_name='EmpruntCd',
            new_name='RentedCd',
        ),
        migrations.RenameModel(
            old_name='EmpruntDvd',
            new_name='RentedDvd',
        ),
    ]
