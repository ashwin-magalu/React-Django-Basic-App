from django.urls import path
from .views import index

app_name = 'frontend' # this will help in redirect, which we have done in views.py of spotify app

urlpatterns = [
    path('', index, name=''),
    path('join/', index),
    path('create/', index),
    path('room/<str:roomCode>', index),
]