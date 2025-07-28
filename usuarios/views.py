from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
