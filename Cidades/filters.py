import django_filters
from .models import Cidade

class CidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.CharFilter(lookup_expr='icontains')  # Adiciona filtro para estado

    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
