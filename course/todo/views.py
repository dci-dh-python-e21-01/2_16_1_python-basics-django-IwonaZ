from django.shortcuts import render
from todo.forms import ValidateForm


# Create your views here.
from django.shortcuts import render

from todo import models


def todo_view(request, id):
    todo = models.Todo.objects.filter(id=id).first()
    previous_todo = models.Todo.objects.filter(id=id - 1).first()
    next_todo = models.Todo.objects.filter(id=id + 1).first()
    return render(
        request,
        "todo/todo.html",
        {"todo": todo, "previous_todo": previous_todo, "next_todo": next_todo},
    )


def todo_overview(request):

    if request.method == "POST":
        form = ValidateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if username == "admin" and password == "password":
                todos = models.Todo.objects.all()
                return render(request, "todo/overview.html", {"todos": todos})
        else:
            message = "Form needs fixes!"
    else:
        form = ValidateForm()
    return render(request, "todo/validate_form.html", {"form": form})
