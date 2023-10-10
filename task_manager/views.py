from django.contrib import messages
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
        pass