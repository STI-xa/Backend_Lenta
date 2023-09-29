from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet
from .views import (
    CategoryViewSet,
    SalesViewSet,
    ShopViewSet,
    ForecastViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sales', SalesViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'forecast', ForecastViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
