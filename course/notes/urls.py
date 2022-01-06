from django.urls import path
from notes import views

urlpatterns = [
    path("sections/", views.sections, name="sections"),
    path("sections/0", views.sections, name="zero"),
    path("sections/<int:text>", views.numbered_notes, name="numbered_notes"),
    path("sections/<str:text>", views.details, name="details"),
]
