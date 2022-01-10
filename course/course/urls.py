"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from common import views
from notes.views import Search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="common/home.html"), name="home"),
    path(
        "home", TemplateView.as_view(template_name="common/home.html"), name="home_page"
    ),
    path("<int:id>/", views.redirect_id_view),
    path("search/", Search.as_view(), name="search_form"),
    path("notes/", include(("notes.urls", "notes"), namespace="notes")),
    path("todo/", include(("todo.urls", "todo"), namespace="todo")),
]
