from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade
from .serializers import EstadoSerializer, CidadeSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import CidadeFilter
from rest_framework.permissions import IsAuthenticated

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [IsAuthenticated]

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()  # Adicione esta linha
    serializer_class = CidadeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_class = CidadeFilter

    def get_queryset(self):
        return Cidade.objects.filter(dono=self.request.user)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)
