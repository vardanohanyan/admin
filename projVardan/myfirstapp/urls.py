from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='myfirstapp-a'),
    path('about/', views.about, name='myfirstapp-a')
]