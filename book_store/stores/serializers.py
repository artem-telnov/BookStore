from rest_framework import serializers
from books.models import Book
from django.db import models

from stores.models import Store, BookStore


# Группа сериализаторов для корректной записи данных.
class CreateBookStoreSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source="book_id")
    amount = serializers.IntegerField()


class CreateStoreSerializer(serializers.ModelSerializer):
    books = CreateBookStoreSerializer(many=True, source="book_amounts")

    class Meta:
        model = Store
        fields = ["books", "name"]

    def create(self, validated_data):
        books = validated_data.pop("book_amounts")
        store = Store.objects.create(**validated_data)

        for book in books:
            BookStore.objects.create(
                book=book["book_id"], store=store, amount=book["amount"]
            )

        return store

    def update(self, instance, validated_data):
        books = validated_data.pop("book_amounts")
        books_set = {book["book_id"] for book in books}
        self._clear_removed(books_set, instance)

        for book in books:
            BookStore.objects.update_or_create(
                book=book["book_id"],
                store=instance, defaults={"amount": book["amount"]}
            )

        return instance

    def _clear_removed(self, books_set, instance):
        BookStore.objects.filter(
            ~models.Q(book__in=books_set), store=instance).delete()


# Группа сериализаторов для чтения.
class ReadBookStoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="book.id")
    amount = serializers.IntegerField()
    name = serializers.CharField(source="book.name")


class ReadStoreSerializer(serializers.ModelSerializer):
    books = ReadBookStoreSerializer(many=True, source="book_amounts")

    class Meta:
        model = Store
        fields = ["id", "name", "books"]
