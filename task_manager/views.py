from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext_lazy


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')