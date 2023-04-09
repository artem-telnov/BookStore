from django.db import models

from books.models import Book


class Store(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)


class BookStore(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
