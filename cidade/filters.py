import django_filters
from .models import Cidade

class CidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
