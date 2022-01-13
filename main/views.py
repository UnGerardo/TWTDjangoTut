from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def landingPage(request, id):
    currentList = ToDoList.objects.get(id=id)
    return render(request, 'list.html', {'currentList': currentList})

def home(request):
    return render(request, 'home.html', {})