from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from todo import models


def todo_view(request, id):
    todo = models.Todo.objects.filter(id=id).first()
    return render(request, "todo/todo.html", {"todo": todo})


def todo_overview(request):
    todos = models.Todo.objects.all()
    return render(request, "todo/overview.html", {"todos": todos})
