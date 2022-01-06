from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from todo.models import todos


def todo(request, text):
    my_todo = ""
    title = ""
    body = ""
    status = ""
    enum = enumerate(todos, start=1)

    for count, item in enum:
        if count == text:
            title = item["topic"]
            body = item["text"]
            status = item["status"]

    html = f"<html><body><h1>To Do number {text}</h1><h2>{title}</h2><h3>{body}</h3><h4>{status}</h4><p><a href={reverse('todo:todo', args=[text-1])}>Previous To Do</a><a href={reverse('todo:todo', args=[text+1])}>Next To To</a></p></body></html>"

    return HttpResponse(html)
