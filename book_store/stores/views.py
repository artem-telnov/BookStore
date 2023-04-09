from rest_framework import viewsets, status
from rest_framework.response import Response
from stores.models import Store
from stores.serializers import CreateStoreSerializer, ReadStoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReadStoreSerializer
        else:
            return CreateStoreSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            ReadStoreSerializer(instance=serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )
