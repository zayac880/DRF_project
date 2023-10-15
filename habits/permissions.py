from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение для CRUD-операций только владельцам объектов.
    """
    def has_object_permission(self, request, view, objects):
        if request.method in permissions.SAFE_METHODS:
            return True
        return objects.user == request.user


class ReadOnlyForNonOwners(permissions.BasePermission):
    """
    Разрешение только на чтение для пользователей, не являющихся владельцами.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class PublicHabitReadOnly(permissions.BasePermission):
    """
    Разрешение только на чтение для публичных привычек.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class HabitPermissions(permissions.IsAuthenticated):
    """
    Комбинированное разрешение для CRUD-операций над привычками.
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)
