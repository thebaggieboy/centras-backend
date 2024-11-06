from django.shortcuts import render
from rest_framework import viewsets
from .models import Orders
from .serializers import OrderSerializer




class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    