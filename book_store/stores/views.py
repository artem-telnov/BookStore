from rest_framework import viewsets
from stores.models import Store

from stores.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
