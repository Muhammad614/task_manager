from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUserCreationForm
# Create your views here.


def home(request):
    return render(request, 'auth/profile.html')


def register(request):
    form = ProfileUserCreationForm()
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            authenticate(u)
            login(request, u)
            return redirect("/")
        else:
            message = "Incorrect username or password!"
            messages.add_message(request, messages.ERROR, message)
            return render(request, "auth/register.html", {"form": form})
    return render(request, "auth/register.html", {"form": form})


class MyLoginView(LoginView, LoginRequiredMixin):
    template_name = 'auth/login.html'
