from django.urls import path
from . import views
from .views import sign_up

urlpatterns = [
    path('platform', views.store_platform, name='platform'),
    path('goods', views.store_goods, name='goods'),
    path('cart', views.store_cart, name='cart'),
    path('sign_up', sign_up, name='sign_up'),
]
