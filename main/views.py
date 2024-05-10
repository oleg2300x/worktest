from rest_framework import viewsets, permissions

from .models import NetworkElement, Product
from .serializers import NetworkElementSerializer, ProductSerializer


class NetworkElementViewSet(viewsets.ModelViewSet):
    queryset = NetworkElement.objects.all()
    serializer_class = NetworkElementSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
