from rest_framework import serializers
from Aplicativo.models import Atualizacao, Necessitado
from Usuario.models import Usuario


class AtualizacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Atualizacao
        fields = ('att_id','att_usu_id','att_nec_id')

class NecessitadoSerializer(serializers.ModelSerializer):
    necessitado = AtualizacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Necessitado
        fields = ('nec_nome','necessitado')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
