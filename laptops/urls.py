from django.urls import path
from . import views

app_name = 'laptops'
urlpatterns = [
    path('', views.list_laptops, name='list_laptops'),
]
