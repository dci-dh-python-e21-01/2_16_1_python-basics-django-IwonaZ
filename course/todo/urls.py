from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path("", views.todo_overview, name="todo_overview"),
    path("<int:id>/", views.todo_view, name="todo_view"),
]
