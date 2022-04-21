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


class StockCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Stock


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Pedido


class AgregarDetallePedidoSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(min_value=1)
    pedidoId = serializers.IntegerField(min_value=1)
    platoId = serializers.IntegerField(min_value=1)
