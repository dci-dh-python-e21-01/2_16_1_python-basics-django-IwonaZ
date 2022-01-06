from django.urls import path
from todo import views

urlpatterns = [
    path("<int:text>", views.todo, name="todo"),
    path("0", views.todo, name="zero"),
]
