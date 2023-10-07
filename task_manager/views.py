from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext_lazy
from .forms import UsersCreateForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UsersCreateForm()
        return render(request, 'users_create.html', {
            'form': form,
        })