from unicodedata import name
from django.urls import path
from main.views import landingPage, home, create

urlpatterns = [
    path('<int:id>/', landingPage, name='landing page'),
    path('', home, name='home'),
    path('create/', create, name='create')
]