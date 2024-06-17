from django.urls import path

from .views import DisponibilidadeViewSet, DisponExcecaoViewSet, EmpreendimentoViewSet, LocalidadeViewSet

urlpatterns = [
    path('getDisponibilidade', DisponibilidadeViewSet.list_disponibilidade, name='getDisponibilidade'),
    path('getDisponibilidade/<int:id>/', DisponibilidadeViewSet.get_disponibilidade, name='getDisponibilidadeId'),
    path('postDisponibilidade', DisponibilidadeViewSet.post_disponibilidade, name='postDisponibilidade'),
    path('patchDisponibilidade/<int:id>/', DisponibilidadeViewSet.patch_disponibilidade, name='patchDisponibilidade'),
    path('deleteDisponibilidade/<int:id>/', DisponibilidadeViewSet.delete_disponibilidade, name='deleteDisponibilidade'),

    path('getDisponExcecao', DisponExcecaoViewSet.list_disponibilidade_excecao, name='getDisponExcecao'),
    path('getDisponExcecao/<int:id>/', DisponExcecaoViewSet.get_disponibilidade_excecao, name='getDisponExcecaoId'),
    path('postDisponExcecao', DisponExcecaoViewSet.post_disponibilidade_excecao, name='postDisponExcecao'),
    path('patchDisponExcecao/<int:id>/', DisponExcecaoViewSet.patch_disponibilidade_excecao, name='patchDisponExcecao'),
    path('deleteDisponExcecao/<int:id>/', DisponExcecaoViewSet.delete_disponibilidade_excecao, name='deleteDisponExcecao'),

    path('getEmpreendimento', EmpreendimentoViewSet.list_empreendimento, name='getEmpreendimento'),
    path('getLocalidade', LocalidadeViewSet.list_localidade, name='getLocalidade')
]