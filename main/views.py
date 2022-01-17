from urllib import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def list(request, id):
    currentList = ToDoList.objects.get(id=id)

    #request.POST has all the info of the form
    #NEED TO RESEARCH BUG WHERE REFRESH CAUSES POST REQUEST TO BE DUPLICATED CREATING DUPLICATE ITEMS
    if request.method == "POST":
        print(request.POST)
        #choose a specific button, will have no value or the value defined in the value attribute
        if request.POST.get("save"):
            for item in currentList.item_set.all():
                #I think this works because unchecked checkboxes don't get sent in the POST request and aren't seen, the ones that checked are tied to the value 'clicked'
                #right so only filled out fields are included in the POST request
                if request.POST.get(f"c{item.id}") == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        
        elif request.POST.get("newItem"):
            text = request.POST.get("new")
            if len(text) > 2:
                currentList.item_set.create(text=text, complete=False)
            else:
                print(f"'{text}' is invalid.")
            

    return render(request, 'list.html', {'currentList': currentList})

def home(request):
    return render(request, 'home.html', {})

def create(request):
    #get user info with request.user

    #when form is submitted
    if request.method == "POST":
        #takes the form input from the request and creates an object containing the data fields
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        #redirects to new table
        return HttpResponseRedirect(f"/{t.id}")
    
    #when form page is accessed
    else:
        form = CreateNewList()
    return render(request, 'create.html', {"form": form})