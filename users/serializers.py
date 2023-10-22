from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализация для модели User.
    """
    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'city',
            'avatar',
            'password'
        )
