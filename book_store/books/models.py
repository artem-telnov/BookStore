from django.db import models


class Book(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)
    # TODO После создания таблицы авторов, добавить связь!
