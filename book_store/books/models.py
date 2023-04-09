from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, blank=False)
