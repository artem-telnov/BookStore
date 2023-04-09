from rest_framework.routers import DefaultRouter

from stores.views import StoreViewSet

router = DefaultRouter()

router.register("", StoreViewSet)

urlpatterns = router.urls
