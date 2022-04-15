from rest_framework import serializers
from .models import Plato


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plato
