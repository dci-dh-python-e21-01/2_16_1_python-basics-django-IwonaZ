from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, CreateView, UpdateView
from django.urls import reverse
from notes import models
from notes.models import Section
from notes.forms import SearchForm
import logging

logger = logging.getLogger("django")


def notes_main_view(request):
    logger.info("User has visited page./ Info log")
    logger.debug(request)
    logger.warning(request, "This is a worning log")
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


# def search_view(request, search_text):
#     section = models.Section.objects.filter(note__icontains=search_text).first()
#     return render(
#         request, "notes/search.html", {"section": section, "term": search_text}
#     )


class SearchResultsView(TemplateView):

    template_name = "notes/search_term.html"

    def get_context_data(self, search_term):
        sections = models.Section.objects.all()

        return {"sections": sections, "search_term": search_term}


# class SearchView(FormView):
#     template_name = "notes/search_form.html"
#     form_class = SearchForm

#     def get_success_url(self):
#         term_of_search = self.kwargs["term_of_search"]
#         return reverse("notes:search", args=[term_of_search])

#     def get_context_data(self, *args, **kwargs):
#         return {"my_form": SearchForm()}


def form_view(request):
    success_message = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        is_valid = form.is_valid()
        if is_valid:
            searched_term = request.POST.get("term_of_search")
            section = request.POST.get("section")
            return redirect(reverse("notes:search", args=(searched_term,)))
        else:
            message = "Form needs fixes!"
    else:
        form = SearchForm()
    return render(
        request,
        "notes/search_form.html",
        {"success_message": success_message, "form": form},
    )


class NoteCreateView(CreateView):
    model = Section
    fields = ["title", "note", "slug"]

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def form_valid(self, form):
    #     form.slug = self.request.form.get("title")
    #     return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Section
    fields = ["title", "note", "slug"]
