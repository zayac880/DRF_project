from rest_framework.exceptions import ValidationError


def validate_related_habit_and_reward(related_habit, reward):
    if related_habit and reward:
        raise ValidationError("Нельзя одновременно выбирать связанную привычку и указывать вознаграждение.")


def validate_execution_time(execution_time):
    if execution_time > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")


def validate_related_habit_is_nice_habit(related_habit, nice_habit):
    if related_habit and not nice_habit:
        raise ValidationError("Связанная привычка должна быть приятной привычкой.")


def validate_nice_habit(nice_habit, related_habit, reward):
    if nice_habit and (related_habit or reward):
        raise ValidationError("У приятной привычки не может быть связанной привычки или вознаграждения.")


def validate_periodicity(periodicity):
    if periodicity > 7:
        raise ValidationError("Привычку нельзя выполнять реже, чем 1 раз в 7 дней.")
