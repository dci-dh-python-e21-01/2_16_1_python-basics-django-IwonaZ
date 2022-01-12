from django.test import TestCase
from notes.models import Section


class TestModels(TestCase):
    def setUp(self):
        self.note1 = Section.objects.create(
            title="Web Frameworks", note="Test", slug="test"
        )

    def test_absolute_url(self):
        self.assertEqual(self.note1.get_absolute_url(), "/notes/1/")
