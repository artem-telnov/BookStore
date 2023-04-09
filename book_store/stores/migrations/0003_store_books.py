# Generated by Django 4.2 on 2023-04-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("stores", "0002_bookstore"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="books",
            field=models.ManyToManyField(
                related_name="stores", through="stores.BookStore", to="books.book"
            ),
        ),
    ]