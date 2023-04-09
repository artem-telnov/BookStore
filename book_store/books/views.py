from rest_framework import viewsets
from books.models import Book

from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
