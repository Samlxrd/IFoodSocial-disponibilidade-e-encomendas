from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class DisponibilidadeViewSet(ModelViewSet):
    queryset = Disponibilidade.objects.all()
    serializer_class = [DisponibilidadeSerializer, DisponibilidadeViewSerializer]
    
    @api_view(['GET'])
    def list_disponibilidade(request):
        disponibilidade = Disponibilidade.objects.all()
        serializer = DisponibilidadeViewSerializer(disponibilidade, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def get_disponibilidade(request, id):
        disponibilidade = Disponibilidade.objects.get(cod_disponibilidade=id)
        serializer = DisponibilidadeViewSerializer(disponibilidade)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post_disponibilidade(request):
        cod_localidade = request.data.get('cod_localidade')
        serializer = DisponibilidadeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    def patch_disponibilidade(request, id):
        disponibilidade = Disponibilidade.objects.get(cod_disponibilidade=id)
        serializer = DisponibilidadeSerializer(disponibilidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def delete_disponibilidade(request, id):
        disponibilidade = Disponibilidade.objects.get(cod_disponibilidade=id)
        disponibilidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisponExcecaoViewSet(ModelViewSet):
    queryset = DisponExcecao.objects.all()
    serializer_class = DisponExcecaoSerializer

    @api_view(['GET'])
    def list_disponibilidade_excecao(request):
        disponibilidade_excecao = DisponExcecao.objects.all()
        serializer = DisponExcecaoViewSerializer(disponibilidade_excecao, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def get_disponibilidade_excecao(request, id):
        disponibilidade_excecao = DisponExcecao.objects.get(cod_dispon_excecao=id)
        serializer = DisponExcecaoViewSerializer(disponibilidade_excecao)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post_disponibilidade_excecao(request):
        serializer = DisponExcecaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    def patch_disponibilidade_excecao(request, id):
        disponibilidade_excecao = DisponExcecao.objects.get(cod_dispon_excecao=id)
        serializer = DisponExcecaoSerializer(disponibilidade_excecao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def delete_disponibilidade_excecao(request, id):
        disponibilidade_excecao = DisponExcecao.objects.get(cod_dispon_excecao=id)
        disponibilidade_excecao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmpreendimentoViewSet(ModelViewSet):
    @api_view(['GET'])
    def list_empreendimento(request):
        empreendimento = Empreendimento.objects.all()
        serializer = EmpreendimentoSerializer(empreendimento, many=True)
        return Response(serializer.data)

class LocalidadeViewSet(ModelViewSet):
    @api_view(['GET'])
    def list_localidade(request):
        localidade = Localidade.objects.all()
        serializer = LocalidadeSerializer(localidade, many=True)
        return Response(serializer.data)
    
   
class EntregaViewSet(ModelViewSet):
    queryset = Entrega.objects.all()
    
    @api_view(['POST'])
    def post_entrega(request):
        serializer = EntregaSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoViewSet(ModelViewSet):
    @api_view(['GET'])
    def list_pedido(request):
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)