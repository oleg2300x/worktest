from .apps import MainConfig
from django.urls import path, include
from rest_framework import routers

from .views import NetworkElementViewSet, ProductViewSet

app_name = MainConfig.name

router = routers.DefaultRouter()
router.register(r'network-elements', NetworkElementViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]