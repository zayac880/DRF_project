from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """
    Административная панель для модели User.
    Этот класс определяет, как модель User будет отображаться и фильтроваться
    в административной панели Django.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)

