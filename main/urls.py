from unicodedata import name
from django.urls import path
from main.views import list, home, create, view

urlpatterns = [
    path('<int:id>/', list, name='list'),
    path('home/', home, name='home'),
    path('create/', create, name='create'),
    path('view/', view, name='view'),
]