from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from common import views as common_views
from notes import views as notes_views
from todo import views as todo_views


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_register_url_resolves(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func, common_views.register)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_redirect_url_resolves(self):
        url = reverse("redirect_view", args=[3])
        self.assertEquals(resolve(url).func, common_views.redirect_id_view)

    def test_search_form_url_resolves(self):
        url = reverse("search_form")
        self.assertEquals(resolve(url).func, notes_views.form_view)

    def test_main_notes_url_resolves(self):
        url = reverse("notes:notes_main")
        self.assertEquals(resolve(url).func, notes_views.notes_main_view)

    def test_notes_new_url_resolves(self):
        url = reverse("notes:notes_new")
        self.assertEquals(resolve(url).func.view_class, notes_views.NoteCreateView)

    def test_section_overview_url_resolves(self):
        url = reverse("notes:section_overview")
        self.assertEquals(resolve(url).func, notes_views.section_overview)

    def test_section_details_url_resolves(self):
        url = reverse("notes:section_details", args=["same section"])
        self.assertEquals(resolve(url).func, notes_views.section_details)

    def test_section_view_url_resolves(self):
        url = reverse("notes:section_view", args=["unique-slug"])
        self.assertEquals(resolve(url).func, notes_views.section_view)

    def test_section_id_view_url_resolves(self):
        url = reverse("notes:section_id_view", args=[5])
        self.assertEquals(resolve(url).func, notes_views.section_id_view)

    def test_notes_update_url_resolves(self):
        url = reverse("notes:notes_update", args=[1])
        self.assertEquals(resolve(url).func.view_class, notes_views.NoteUpdateView)

    def test_search_url_resolves(self):
        url = reverse("notes:search", args=["web"])
        self.assertEquals(resolve(url).func.view_class, notes_views.SearchResultsView)

    def test_todo_overview_url_resolves(self):
        url = reverse("todo:todo_overview")
        self.assertEquals(resolve(url).func, todo_views.todo_overview)

    def test_todo_view_url_resolves(self):
        url = reverse("todo:todo_view", args=[1])
        self.assertEquals(resolve(url).func, todo_views.todo_view)
