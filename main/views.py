from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def landingPage(request, id):
    currentList = ToDoList.objects.get(id=id)
    return render(request, 'list.html', {'currentList': currentList})

def home(request):
    return render(request, 'home.html', {})

def create(request):
    #when form is submitted
    if request.method == "POST":
        #takes the form input from the request and creates an object containing the data fields
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
    #when form page is accessed
    else:
        form = CreateNewList()
    return render(request, 'create.html', {"form": form})