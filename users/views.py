from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class CustomPermission(permissions.BasePermission):
    """
    Пользователи могут выполнять регистрацию и авторизацию без аутентификации,
    но для других операций требуется аутентификация.
    """
    def has_permission(self, request, view):
        if view.action in ['create', 'token']:
            return True
        return request.user and request.user.is_authenticated


class UsersViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с моделью User.
    Этот класс определяет представление, которое обрабатывает запросы для модели User.
    Он наследует viewsets.ModelViewSet из Django REST framework и предоставляет
    стандартные CRUD-операции для модели User.
    """
    permission_classes = [CustomPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):

        email = request.data.get('email')
        password = request.data.get('password')
        hashed_password = make_password(password)
        User = get_user_model()

        user = User(email=email, password=hashed_password)
        user.save()
        return Response({'message': 'Пользователь успешно зарегистрирован!'}, status=status.HTTP_201_CREATED)
