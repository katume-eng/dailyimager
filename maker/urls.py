from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.init, name='init'),
    path('users/', views.user_list, name='user_list'),
    path('products/', views.product_list, name='product_list'),
]
