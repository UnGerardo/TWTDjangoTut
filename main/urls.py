from django.urls import path
from main.views import landingPage

urlpatterns = [
    path('', landingPage, name='LandingPage'),
]