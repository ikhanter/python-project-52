from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext_lazy
from .forms import LoginForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(label_suffix='')
        return render(request, 'login.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])  # noqa: E501
        if user:
            messages.add_message(request, messages.SUCCESS, gettext_lazy('You are logged in.'))  # noqa: E501
            login(request, user)
            return redirect('index')
        messages.add_message(request, messages.ERROR, gettext_lazy('Your username and password didn\'t match. Please try again.'))  # noqa: E501
        return redirect('login')


class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class AboutView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
