from django.db import models
from django.contrib.auth.models import User

#delete pycache and sql/lite database file and everything in migrations folder except init.py to reset migrations

# Create your models here.
class ToDoList(models.Model):
    #related name field is the name by which the ToDoList model will be accessed by the foreign key "User"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    

class Item(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text