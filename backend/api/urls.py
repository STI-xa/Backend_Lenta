from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
