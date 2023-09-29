from rest_framework import permissions
from djoser.views import UserViewSet

from .models import CustomUser
from .serializers import (
    CustomUserSerializer
)


class CustomUserViewSet(UserViewSet):
    """Вьюсет модели Юзера."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
