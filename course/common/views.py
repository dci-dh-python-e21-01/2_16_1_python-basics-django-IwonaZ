from django.shortcuts import render, redirect, reverse


def overview_view(request):
    return render(request, "home.html")


def redirect_id_view(request, id):
    return redirect(reverse("section_id_view", args=(id)))
