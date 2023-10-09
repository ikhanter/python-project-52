from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext_lazy
from .forms import UsersCreateForm, LoginForm
from django.contrib.auth.models import User


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UsersCreateForm(label_suffix='')
        return render(request, 'users_create.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = UsersCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('User was created successfully.'))
            return redirect('login')
        messages.add_message(request, messages.ERROR, gettext_lazy('User is not created. Please, check the fields.'))
        return render(request, 'users_create.html', {
            'form': form,
        })
    
class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(label_suffix='')
        return render(request, 'login.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        pass