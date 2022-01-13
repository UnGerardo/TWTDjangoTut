from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def landingPage(request, id):
    # try:
    #     return HttpResponse(f"<h1>{ToDoList.objects.get(id=1).item_set.get(id=id)}</h1>")
    # except:
    #     return HttpResponse(f"<h1>An item with id: {id} doesn't exist.</h1>")
    return render(request, 'base.html', {})

def home(request):
    return render(request, 'home.html', {})