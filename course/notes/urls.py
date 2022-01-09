from django.urls import path
from notes import views

urlpatterns = [
    path("", views.notes_main_view, name="notes_main"),
    path("sections/", views.section_overview, name="section_overview"),
    path("sections/<slug:unique_slug>/", views.section_view, name="section_view"),
    path("<int:id>/", views.section_id_view, name="section_id_view"),
    path("<str:search_text>/", views.search_view),
]
