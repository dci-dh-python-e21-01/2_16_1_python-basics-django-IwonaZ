from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse
from notes import models
from notes.forms import SearchForm


def notes_main_view(request):
    return render(request, "notes/main_overview.html")


def section_overview(request):
    sections = models.Section.objects.all()

    return render(
        request,
        "notes/sections_overview.html",
        {"sections": sections},
    )


def section_details(request, section_name):
    notes = models.Section.objects.filter(title=section_name)
    return render(
        request,
        "notes/section_details.html",
        {"notes": notes, "section_name": section_name},
    )


def section_view(request, unique_slug):
    section = models.Section.objects.filter(slug=unique_slug).first()
    return render(request, "notes/section.html", {"section": section})


def section_id_view(request, id):
    section = models.Section.objects.filter(id=id).first()
    previous_section = models.Section.objects.filter(id=id - 1).first()
    next_section = models.Section.objects.filter(id=id + 1).first()
    return render(
        request,
        "notes/section.html",
        {
            "section": section,
            "next_section": next_section,
            "previous_section": previous_section,
        },
    )


def search_view(request, search_text):
    section = models.Section.objects.filter(note__icontains=search_text).first()
    return render(
        request, "notes/search.html", {"section": section, "term": search_text}
    )


class Search(FormView):
    template_name = "notes/search_form.html"
    form_class = SearchForm

    def get_success_url(self):
        term_of_search = self.kwargs["term_of_search"]
        return reverse("notes:search_text", args=[term_of_search])

    def get_context_data(self, *args, **kwargs):
        return {"my_form": SearchForm()}
