from django.urls import path
from todo import views

urlpatterns = [
    path("<int:text>", views.todo, name="todo"),
    path("0", views.todo, name="zero"),
    path("1", views.todo, name="one"),
]
