from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, registerForm
from django.contrib.auth import authenticate, login, logout

def home_view(request):

    sayfaAdi = "Anasayfa"
    return render(request, "home.html", {"sayfaAdi": sayfaAdi})

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)

        return HttpResponseRedirect("/")
    return render(request, "login.html", {"form": form})

def register_view(request):
    form = registerForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        return HttpResponseRedirect("/")

    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/")


# Create your views here.
