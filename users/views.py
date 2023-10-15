from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с моделью User.
    Этот класс определяет представление, которое обрабатывает запросы для модели User.
    Он наследует viewsets.ModelViewSet из Django REST framework и предоставляет
    стандартные CRUD-операции для модели User.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

