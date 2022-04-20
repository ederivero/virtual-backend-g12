from rest_framework import serializers
from .models import Plato, Stock
from fact_electr.models import Pedido


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plato


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Stock
        depth = 1


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Pedido
