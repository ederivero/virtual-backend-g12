from rest_framework import serializers
from .models import Plato, Stock


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plato


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Stock
