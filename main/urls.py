from django.urls import path
from main.views import landingPage

urlpatterns = [
    path('<int:id>/', landingPage, name='LandingPage'),
]