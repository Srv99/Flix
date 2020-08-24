from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Some text here'
        return render(request, self.template_name, {'variableA': variableA})


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        if request.user.is_authenticated:
            print("Already logged in, Redirecting")
            print(request.user)
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login success")
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('login')
        return HttpResponse("This is Login view. POST Request")


class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        if request.user.is_authenticated:
            print("Already logged in, Redirecting")
            print(request.user)
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            new_user = User(username=username, password=password,
                            email=email, first_name=first_name, last_name=last_name)
            check_email = User.objects.filter(email__iexact=email)
            check_username = User.objects.filter(username__iexact=username)
            if check_email:
                return HttpResponse("Email already registered.")
            elif check_username:
                return HttpResponse("Username already registered")
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse("This is Register view. POST Request")


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return HttpResponse("This is index view. POST Request")
