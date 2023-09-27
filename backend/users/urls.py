from django.urls import include, path
from rest_framework import routers
from djoser.views import UserViewSet

app_name = 'users'

v1_router = routers.DefaultRouter()

v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
