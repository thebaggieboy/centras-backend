from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dashboard

class DashboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'total_earnings', 'total_orders', 'total_deliveries', 'canceled_orders', ]


