# Generated by Django 5.0.6 on 2024-07-03 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_genre_genre_name_case_insensitive_unique_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
