from django.urls import path, include
from .views import CategoryView, SalesView, ShopView, ForecastView
from rest_framework import routers

from users.views import CustomUserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
# router.register(r'categories', SKUViewSet)
# router.register(r'sales', SalesViewSet)
# router.register(r'shops', ShopViewSet)
# router.register(r'forecast', ForecastViewSet)


urlpatterns = [
    path('categories', CategoryView, name='categories'),
    path('sales', SalesView, name='sales'),
    path('shops', ShopView, name='shops'),
    path('forecast', ForecastView, name='forecast'),
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
