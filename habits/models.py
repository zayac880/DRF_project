from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    name = models.CharField(max_length=100, verbose_name='название')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.TextField(verbose_name='действие')
    nice_habit = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL, verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='вознаграждение')
    execution_time = models.PositiveIntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} ч. в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
