from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random_word/', views.random_word, name='random_word'),
]