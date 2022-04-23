from rest_framework import serializers
from .models import Comprobante


class GenerarComprobanteSerializer(serializers.Serializer):
    tipo_de_comprobante = serializers.IntegerField(max_value=4, min_value=1)

    tipo_documento = serializers.ChoiceField(
        required=False, choices=[('RUC', 'RUC'), ('DNI', 'DNI')])

    numero_documento = serializers.CharField(required=False)

    pedido_id = serializers.IntegerField()


class ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = '__all__'
