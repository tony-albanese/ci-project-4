# Generated by Django 3.2.16 on 2023-01-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0008_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='posted_on',
            field=models.DateField(auto_now=True),
        ),
    ]
