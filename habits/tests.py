from django.test import TestCase
from habits.models import Habit
from users.models import User
from django.urls import reverse
from rest_framework.test import APIClient


class HabitTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='testuser@email',
            password='testpassword',
        )
        self.client.force_authenticate(
            user=self.user
        )

    def test_create_habit(self):
        habit_data = {
            'name': 'Новая привычка',
            'place': 'Где-то',
            'time': '12:00',
            'action': 'Что-то делать',
            'nice_habit': True,
            'periodicity': 7,
            'execution_time': 30,
            'user': self.user.id,
        }

        url = reverse('habits:habit-create')
        response = self.client.post(url, habit_data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(Habit.objects.count(), 1)

    def test_list_habits(self):
        habit1 = Habit.objects.create(
            name='Привычка 1',
            place='Где-то',
            time='12:00',
            action='Делать что-то',
            nice_habit=True,
            periodicity=7,
            execution_time=30,
            user=self.user
        )
        habit2 = Habit.objects.create(
            name='Привычка 2',
            place='Где-то еще',
            time='15:00',
            action='Делать что-то еще',
            nice_habit=False,
            periodicity=3,
            execution_time=45,
            user=self.user
        )

        url = reverse('habits:habit-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['count'], 2)

    def test_update_habit(self):
        habit = Habit.objects.create(
            name='Привычка 1',
            place='Где-то',
            time='12:00',
            action='Делать что-то',
            nice_habit=True,
            periodicity=7,
            execution_time=30,
            user=self.user)

        new_data = {
            'name': 'Измененная привычка',
            'place': 'Новое место',
            'time': '14:00',
            'action': 'Другое действие',
            'nice_habit': False,
            'periodicity': 3,
            'execution_time': 45,
            'user': self.user.id,
        }

        url = reverse('habits:habit-update', kwargs={'pk': habit.id})
        response = self.client.put(url, new_data)

        self.assertEqual(response.status_code, 200)

        habit.refresh_from_db()

    def test_delete_habit(self):
        # Create a Habit
        habit = Habit.objects.create(
            name='To be deleted',
            place='Somewhere',
            time='12:00',
            action='Do something',
            nice_habit=True,
            periodicity=7,
            execution_time=30,
            user=self.user
        )

        url = reverse('habits:habit-destroy', kwargs={'pk': habit.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

        self.assertFalse(Habit.objects.filter(id=habit.id).exists())
