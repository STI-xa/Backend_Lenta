from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователя."""

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'username',
            'password',
        )
