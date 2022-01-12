from django.test import TestCase, Client
from django.urls import reverse
from notes import models as notes_models
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.section1 = notes_models.Section.objects.create(
            title="Web Frameworks",
            note="Note about web frameworks",
            slug="web-framework-1",
        )

    def test_notes_main_view(self):
        response = self.client.get(reverse("notes:notes_main"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/main_overview.html")

    def test_section_overview_view(self):
        response = self.client.get(reverse("notes:section_overview"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/sections_overview.html")

    def test_section_details(self):
        response = self.client.get(
            reverse("notes:section_details", args=["Web Frameworks"])
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/section_details.html")

    def test_section_view(self):
        response = self.client.get(
            reverse("notes:section_view", args=["web-framework-1"])
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/section.html")

    def test_section_id_view(self):
        response = self.client.get(reverse("notes:section_id_view", args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/section.html")

    def test_search_results_view_GET(self):
        response = self.client.get(reverse("notes:search", args=["web"]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/search_term.html")

    def test_note_create_POST(self):
        note = notes_models.Section.objects.create(
            title="URL Mapping",
            note="Test text",
            slug="url-mapping-1",
        )
        url = reverse("notes:notes_new")

        response = self.client.post(
            url, {"title": "URL Mapping", "note": "Test text", "slug": "url-mapping-1"}
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(note.title, "URL Mapping")

    def test_login(self):
        self.login_details = {"username": "admin", "password": "password"}
        self.user = User.objects.create_user(**self.login_details)
        url = reverse("login")
        response = self.client.post(url, self.login_details, follow=True)
        self.assertEquals(
            response.status_code,
            200,
        )
        self.assertTrue(response.context["user"].is_authenticated)

    def test_not_logged_in_register_button(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertContains(response, "Register")

    def test_logged_in_register_button(self):
        url = reverse("home")
        self.user = User.objects.create_user(username="admin", password="password")
        self.client.login(username="admin", password="password")
        response = self.client.get(url)
        self.assertNotContains(response, "Register")

    def test_not_logged_in_login_button(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertContains(response, "Login")

    def test_logged_in_login_button(self):
        url = reverse("home")
        self.user = User.objects.create_user(username="admin", password="password")
        self.client.login(username="admin", password="password")
        response = self.client.get(url)
        self.assertNotContains(response, "Login")

    def test_not_logged_in_logout_button(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertNotContains(response, "Logout")

    def test_logged_out_logout_button(self):
        url = reverse("home")
        self.user = User.objects.create_user(username="admin", password="password")
        self.client.login(username="admin", password="password")
        response = self.client.get(url)
        self.assertContains(response, "Logout")
