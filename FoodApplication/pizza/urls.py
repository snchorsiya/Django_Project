from django.urls import path
from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('order/', views.order_page, name='order_page'),
]
