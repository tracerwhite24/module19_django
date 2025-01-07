from django.urls import path
from . import views
from .views import sign_up, news, menu
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu, name='menu'),
    path('platform/', views.store_platform, name='platform'),
    path('platform/news/', news, name='news'),
    path('goods/', views.store_goods, name='goods'),
    path('cart/', views.store_cart, name='cart'),
    path('sign_up/', sign_up, name='sign_up'),
]
