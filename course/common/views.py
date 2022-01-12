from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserRegisterForm


def overview_view(request):
    return render(request, "home.html")


def redirect_id_view(request, id):
    return redirect(reverse("section_id_view", args=(id)))


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}! You are now able to login."
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "common/register.html", {"form": form})
