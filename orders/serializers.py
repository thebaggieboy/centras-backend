from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Orders

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'product_name', 'category', 'price', 'quantity', 'status']
