from rest_framework import viewsets, status
from rest_framework.response import Response
from stores.models import Store
from stores.serializers import CreateStoreSerializer, ReadStoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReadStoreSerializer
        return CreateStoreSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            ReadStoreSerializer(instance=serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(
            ReadStoreSerializer(instance=serializer.instance).data
        )
