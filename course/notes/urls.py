from django.urls import path
from notes import views
from notes.views import SearchResultsView, NoteCreateView, NoteUpdateView

urlpatterns = [
    path("", views.notes_main_view, name="notes_main"),
    path("new/", NoteCreateView.as_view(), name="notes_new"),
    path("sections/", views.section_overview, name="section_overview"),
    path("sections/<str:section_name>", views.section_details, name="section_details"),
    path("sections/<slug:unique_slug>/", views.section_view, name="section_view"),
    path("<int:id>/", views.section_id_view, name="section_id_view"),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name="notes_update"),
    # path("<str:search_text>/", views.search_view, name="search_text"),
    path("<str:search_term>/", SearchResultsView.as_view(), name="search"),
]
