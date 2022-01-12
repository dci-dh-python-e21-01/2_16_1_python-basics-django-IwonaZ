from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from common import views
from notes import views as notes_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="common/home.html"), name="home"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="common/logout.html"),
        name="logout",
    ),
    path("<int:id>/", views.redirect_id_view, name="redirect_view"),
    path("search/", notes_views.form_view, name="search_form"),
    path("notes/", include(("notes.urls", "notes"), namespace="notes")),
    path("todo/", include(("todo.urls", "todo"), namespace="todo")),
]
