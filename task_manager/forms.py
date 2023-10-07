from django import forms
from .models import User
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy


class UsersCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': gettext_lazy('Confirm password')}),
        validators=[MinLengthValidator(3)],
        help_text=gettext_lazy('For the password confirmation, please, enter the password one more time.'))

    class Meta:
        model = User
        label_suffix = ''
        fields = ['first_name', 'last_name', 'username', 'password']
        labels = {
            'first_name': gettext_lazy('First name'),
            'last_name': gettext_lazy('Last name'),
            'username': gettext_lazy('Username'),
            'password': gettext_lazy('Password'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': gettext_lazy('First name'), 'class': 'my-3'}),
            'last_name': forms.TextInput(attrs={'placeholder': gettext_lazy('Last name'), 'class': 'my-3'}),
            'username': forms.TextInput(attrs={'placeholder': gettext_lazy('Username'), 'class': 'my-3'}),
            'password': forms.TextInput(attrs={'placeholder': gettext_lazy('Password'), 'class': 'my-3'}),
        }
        help_texts = {
            'username': gettext_lazy('Required field. Max length is 150 symbols. Letters, digits and  @/./+/-/_ symbols are allowed.'),
            'password': gettext_lazy('Your password must contain at least 3 symbols.'),
        }

