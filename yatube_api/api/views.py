# TODO:  Напишите свой вариант
from rest_framework import viewsets

from api.serializers import GroupSerializer
from posts.models import Group


class PostViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
       Получение списка доступных сообществ.
       Получение информации о сообществе по id.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
