from django.urls import path
from .views import (
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit-destroy'),
]
