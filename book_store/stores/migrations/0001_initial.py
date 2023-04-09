# Generated by Django 4.2 on 2023-04-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updateed_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
