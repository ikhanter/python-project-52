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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label_suffix = ''

    def is_valid(self):
        try:
            return super().is_valid()
        except forms.ValidationError:
            self.add_error(
                'name',
                gettext_lazy('Label with this name already exists'),
            )
            return False
