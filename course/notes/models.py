from django.db import models
from django.urls import reverse

SECTION_CHOICES = (
    ("Web Frameworks", "Web Frameworks"),
    ("URL Mapping", "URL Mapping"),
    ("Setting up Django", "Setting up Django"),
)


class Section(models.Model):
    title = models.CharField(max_length=500, choices=SECTION_CHOICES)
    note = models.TextField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("notes:section_id_view", kwargs={"id": self.id})
