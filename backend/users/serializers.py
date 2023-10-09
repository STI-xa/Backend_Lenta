from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""

    class Meta:
        model = CustomUser
        fields = (
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
            'username',
            'email',
            'password',
        )
