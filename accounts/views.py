from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, logout, login
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegisterForm
from django.core.mail import send_mail
# Create your views here.

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect("/")
    return render(request,"accounts/login.html", {"form":form, "title":title} )

def register_view(request):
    title = "Register"
    form  = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password=password)
        login(request, new_user)
        return redirect(reverse('profiles:create'))
    context = {
        "form":form,
        "title":title
    }
    return render(request,"forms.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")


def joinus(request):
    return render(request,'accounts/join_us.html',{})
