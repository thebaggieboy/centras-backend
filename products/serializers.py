from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Products

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'product_name', 'category', 'price', 'quantity', 'status']
