from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
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
            'first_name',
            'last_name',
            'password',
        )
