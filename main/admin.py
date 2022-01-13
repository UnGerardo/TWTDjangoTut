from django.contrib import admin
from .models import ToDoList, Item

# Register your models here. To see on admin page
admin.site.register(ToDoList)
admin.site.register(Item)