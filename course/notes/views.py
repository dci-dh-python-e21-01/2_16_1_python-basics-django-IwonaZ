from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from notes.models import notes


# def home(request):
#     return render(request, "common/home.html")


def sections(request):
    html = f"<html><body><h2>Browse my notes by section</h2><ol><li><a href={reverse('notes:details', args=['Web Frameworks'])}>Web Frameworks</a></li><li><a href={reverse('notes:details', args=['Setting up Django'])}>Setting up Django</a></li><li><a href={reverse('notes:details', args=['URL Mapping'])}>URL Mapping</a></ol><p><a href={reverse('home')}>Back to home</a></p></body></html>"
    return HttpResponse(html)


def details(request, text):
    my_note = ""

    for note in notes:
        if note["section"] == text:
            my_note += f"<li>{note['text']}</li>"

    html = f"<html><body><h2>Notes about {text}</h2><ol>{my_note}</ol><p><a href={reverse('notes:sections')}>Back to sections</a></p></body></html>"

    return HttpResponse(html)


def numbered_notes(request, text):
    my_note = ""
    title = ""
    enum = enumerate(notes, start=1)

    for count, note in enum:
        if count == text:
            title = note["section"]
            my_note = f"{note['text']}"

    html = f"<html><body><h1>Note number {text}</h1><h3>{title}</h3><p>{my_note}</p><p><a href={reverse('notes:numbered_notes', args=[text-1])}>Previous note</a> <a href={reverse('home')}>Back to home</a><a href={reverse('notes:numbered_notes', args=[text+1])}>Next note</a></p></body></html>"

    return HttpResponse(html)


def redirect_note(request, text):
    return redirect("notes:numbered_notes", text=text)  # this redirect view
    # return redirect(reverse("numbered_notes", args=[text]))  # this redirect url
