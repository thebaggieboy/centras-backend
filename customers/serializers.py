from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customers

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'full_name', 'phone_number', 'email_address', 'address', 'status']
