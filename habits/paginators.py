from rest_framework.pagination import PageNumberPagination


class HabitListPagination(PageNumberPagination):
    """
    Пагинация списка привычек.
    Позволяет настроить пагинацию списка привычек с выводом по 5 привычек на страницу.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
