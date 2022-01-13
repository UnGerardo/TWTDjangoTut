from django.urls import path
from main.views import landingPage, home

urlpatterns = [
    path('<int:id>/', landingPage, name='landing page'),
    path('', home, name='home')
]