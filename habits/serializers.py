from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализация для модели привычек.
    Сериализация используется для преобразования объектов модели привычки в JSON-формат и обратно при взаимодействии
    с API.
    """
    class Meta:
        model = Habit
        fields = (
            'id',
            'user',
            'name',
            'place',
            'time',
            'action',
            'nice_habit',
            'related_habit',
            'periodicity',
            'reward',
            'execution_time',
            'is_public'
            )
