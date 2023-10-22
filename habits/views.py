from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from django.core.exceptions import ValidationError

from habits.models import Habit
from habits.paginators import HabitListPagination
from habits.permissions import HabitPermissions, IsOwnerOrReadOnly, PublicHabitReadOnly
from habits.serializers import HabitSerializer
from habits.servises import schedule_notification
from habits.validators import validate_related_habit_and_reward, validate_execution_time, \
    validate_related_habit_is_nice_habit, validate_nice_habit, validate_periodicity


class HabitListAPIView(generics.ListAPIView):
    """
    Представление для просмотра списка привычек.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [HabitPermissions]


class HabitPublicListAPIView(generics.ListAPIView):
    """
    Представление для просмотра списка привычек.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [PublicHabitReadOnly]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для получения информации о конкретной привычке по её идентификатору.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания новой привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    #permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        related_habit = data.get('related_habit')
        reward = data.get('reward')
        execution_time = data.get('execution_time')
        nice_habit = data.get('nice_habit')
        periodicity = data.get('periodicity')

        try:
            validate_related_habit_and_reward(related_habit, reward)
            validate_execution_time(execution_time)
            if related_habit:
                validate_related_habit_is_nice_habit(related_habit, related_habit.nice_habit)
            validate_nice_habit(nice_habit, related_habit, reward)
            validate_periodicity(periodicity)
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        habit = serializer.instance
        telegram_user_id = self.request.user.telegram_user_id
        schedule_notification(habit, telegram_user_id)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления информации о существующей привычке.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [AllowAny]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления привычки по её идентификатору.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]
    