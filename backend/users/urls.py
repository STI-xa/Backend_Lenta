from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework import routers


from .views import UserViewSet

app_name = 'users'

v1_router = routers.DefaultRouter()

v1_router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
   path('', include(v1_router.urls)),
   path('api-token-auth/', views.obtain_auth_token),
]
