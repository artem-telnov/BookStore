# Generated by Django 4.2 on 2023-04-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stores", "0004_alter_bookstore_book_alter_bookstore_store"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="bookstore",
            constraint=models.UniqueConstraint(
                models.F("book"), models.F("store"), name="uniq_book_store"
            ),
        ),
    ]
