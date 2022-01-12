from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def landingPage(request, id):
    try:
        return HttpResponse(f"<h1>{models.ToDoList.objects.get(id=1).item_set.get(id=id)}</h1>")
    except:
        return HttpResponse(f"<h1>An item with id: {id} doesn't exist.</h1>")