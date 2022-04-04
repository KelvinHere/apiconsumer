from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random_word/', views.random_word, name='random_word'),
    path('word_by_pk/', views.word_by_pk, name='word_by_pk'),
    path('update_word/', views.update_word, name='update_word'),
]