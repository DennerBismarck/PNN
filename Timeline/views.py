from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from Aplicativo.models import Atualizacao, Necessitado
from Usuario.models import Usuario
from .serializers import AtualizacaoSerializer, NecessitadoSerializer

@api_view(['GET'])
def getData(request):
    Atualizacoes = Necessitado.objects.all()
    serializer = NecessitadoSerializer(Atualizacoes, many=True)
    return Response(serializer.data)

