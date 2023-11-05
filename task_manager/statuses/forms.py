from django import forms
from .models import Status
from django.utils.translation import gettext_lazy


class StatusesCreateForm(forms.ModelForm):

    class Meta:

        model = Status
        fields = ['name']
        labels = {
            'name': gettext_lazy('Name'),
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('Name'),
                'class': 'mb-3',
            })
        }
