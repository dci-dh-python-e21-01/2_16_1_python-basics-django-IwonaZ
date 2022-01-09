from django.shortcuts import render

from notes import models


def notes_main_view(request):
    return render(request, "notes/main_overview.html")


def section_overview(request):
    sections = models.Section.objects.all()

    return render(
        request,
        "notes/overview.html",
        {"sections": sections},
    )


def section_view(request, unique_slug):
    section = models.Section.objects.filter(slug=unique_slug).first()
    return render(request, "notes/section.html", {"section": section})


def section_id_view(request, id):
    section = models.Section.objects.filter(id=id).first()
    return render(request, "notes/section.html", {"section": section})


def search_view(request, search_text):
    section = models.Section.objects.filter(note__icontains=search_text).first()
    return render(
        request, "notes/search.html", {"section": section, "term": search_text}
    )
