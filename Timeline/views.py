from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from Aplicativo.models import Atualizacao
from .serializers import AtualizacaoSerializer

@api_view(['GET'])
def getData(request):
    Atualizacoes = Atualizacao.objects.all()
    serializer = AtualizacaoSerializer(Atualizacoes, many=True)
    return Response(serializer.data)

