from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters import rest_framework as Dfilters

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [Dfilters.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ativo',]
    ordering_fields = ['nome',]
    search_fields = ['nome', 'cpf']