from rest_framework import serializers
from Aplicativo.models import Atualizacao

class AtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Atualizacao
        fields = '__all__'