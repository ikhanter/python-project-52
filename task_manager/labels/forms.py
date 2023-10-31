from django import forms
from django.utils.translation import gettext_lazy
from .models import Label


class LabelsCreateForm(forms.ModelForm):

    class Meta:

        model = Label
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': gettext_lazy('Name'),
                }
            )
        }
        labels = {
            'name': gettext_lazy('Name'),
        }
