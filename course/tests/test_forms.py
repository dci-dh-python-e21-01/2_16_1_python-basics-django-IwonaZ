from django.test import SimpleTestCase
from todo.forms import ValidateForm
from notes.forms import SearchForm


class TestForms(SimpleTestCase):
    def test_validate_form_valid_data(self):
        form = ValidateForm(data={"username": "admin", "password": "password"})

        self.assertTrue(form.is_valid())

    def test_validate_form_no_data(self):
        form = ValidateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_search_form_valid_data(self):
        form = SearchForm(data={"term_of_search": "web", "section": "Web Frameworks"})

        self.assertTrue(form.is_valid())

    def test_search_form_no_data(self):
        form = SearchForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
