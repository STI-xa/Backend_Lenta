from django.urls import path, include
from rest_framework import routers

from users.views import CustomUserViewSet
from .views import (
    SKUViewsSet,
    SalesViewSet,
    ShopViewSet,
    ForecastViewSet
)


app_name = 'api'


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'categories', SKUViewsSet, basename='sku')
router.register(r'sales', SalesViewSet, basename='sale')
router.register(r'shops', ShopViewSet, basename='shop')
router.register(r'forecast', ForecastViewSet, basename='forecast')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.authtoken'))
]

# path('v1/forecast/', ForecastView.as_view(), name='forecast'),
