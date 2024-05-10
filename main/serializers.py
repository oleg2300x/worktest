from rest_framework import serializers

from .models import NetworkElement, Product


class NetworkElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkElement
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
