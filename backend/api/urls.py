from django.urls import path
from .views import CategoryView, SalesView, ShopView, ForecastView

app_name = 'api'


urlpatterns = [
    path('categories', CategoryView, name='categories'),
    path('sales', SalesView, name='sales'),
    path('shops', ShopView, name='shops'),
    path('forecast', ForecastView, name='forecast'),
]
