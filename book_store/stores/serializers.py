from rest_framework import serializers
from books.models import Book

from stores.models import Store, BookStore


# Группа сериализаторов для корректной записи данных.
class CreateBookStoreSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    amount = serializers.IntegerField()


class CreateStoreSerializer(serializers.ModelSerializer):
    books = CreateBookStoreSerializer(many=True)

    class Meta:
        model = Store
        fields = ["books", "name"]

    def create(self, validated_data):
        books = validated_data.pop("books")
        store = Store.objects.create(**validated_data)

        for book in books:
            BookStore.objects.create(
                book=book["id"], store=store, amount=book["amount"]
            )

        return store


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
