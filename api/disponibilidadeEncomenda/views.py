from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class DisponibilidadeViewSet(ModelViewSet):
    queryset = Disponibilidade.objects.all()
    serializer_class = DisponibilidadeSerializer
    
    @api_view(['GET'])
    def list_disponibilidade(request):
        disponibilidade = Disponibilidade.objects.all()
        serializer = DisponibilidadeSerializer(disponibilidade, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def get_disponibilidade(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        serializer = DisponibilidadeSerializer(disponibilidade)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post_disponibilidade(request):
        serializer = DisponibilidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    def patch_disponibilidade(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        serializer = DisponibilidadeSerializer(disponibilidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def delete_disponibilidade(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        disponibilidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisponExcecaoViewSet(ModelViewSet):
    queryset = DisponExcecao.objects.all()
    serializer_class = DisponExcecaoSerializer

    @api_view(['GET'])
    def list_disponibilidade_excecao(request):
        disponibilidade_excecao = DisponExcecao.objects.all()
        serializer = DisponExcecaoSerializer(disponibilidade_excecao, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def get_disponibilidade_excecao(request, pk):
        disponibilidade_excecao = DisponExcecao.objects.get(pk=pk)
        serializer = DisponExcecaoSerializer(disponibilidade_excecao)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post_disponibilidade_excecao(request):
        serializer = DisponExcecaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    def patch_disponibilidade_excecao(request, pk):
        disponibilidade_excecao = DisponExcecao.objects.get(pk=pk)
        serializer = DisponExcecaoSerializer(disponibilidade_excecao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def delete_disponibilidade_excecao(request, pk):
        disponibilidade_excecao = DisponExcecao.objects.get(pk=pk)
        disponibilidade_excecao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)