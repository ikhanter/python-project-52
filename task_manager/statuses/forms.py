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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label_suffix = ''

    def is_valid(self):
        try:
            return super().is_valid()
        except forms.ValidationError:
            self.add_error(
                'name',
                gettext_lazy('Status with this name already exists'),
            )
            return False
