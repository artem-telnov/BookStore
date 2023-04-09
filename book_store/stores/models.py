from django.db import models

from books.models import Book
from django.db.models import UniqueConstraint


class Store(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(
        through="BookStore", to=Book, related_name="stores")


class BookStore(models.Model):
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name="book_amounts_in_store"
    )
    store = models.ForeignKey(
        to=Store, on_delete=models.CASCADE, related_name="book_amounts"
    )
    amount = models.PositiveIntegerField()

    class Meta:
        constraints = [
            UniqueConstraint("book", "store", name="uniq_book_store"),
        ]
