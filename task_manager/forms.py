from django import forms
from .models import User
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy


class UsersCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': gettext_lazy('Confirm password')}),
        validators=[MinLengthValidator(3)],
        help_text=gettext_lazy('For the password confirmation, please, enter the password one more time.'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'USERNAME_FIELD', 'PASSWORD_FIELD']
        labels = {
            'first_name': gettext_lazy('First name'),
            'last_name': gettext_lazy('Last name'),
            'USERNAME_FIELD': gettext_lazy('Username'),
            'PASSWORD_FIELD': gettext_lazy('Password'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': gettext_lazy('First name'), 'class': 'mb-3'}),
            'last_name': forms.TextInput(attrs={'placeholder': gettext_lazy('Last name'), 'class': 'mb-3'}),
            'USERNAME_FIELD': forms.TextInput(attrs={'placeholder': gettext_lazy('Username'), 'class': 'mb-3'}),
            'PASSWORD_FIELD': forms.PasswordInput(attrs={'placeholder': gettext_lazy('Password')}),
        }
        help_texts = {
            'USERNAME_FIELD': gettext_lazy('Required field. Max length is 150 symbols. Letters, digits and  @/./+/-/_ symbols are allowed.'),
            'PASSWORD_FIELD': gettext_lazy('Your password must contain at least 3 symbols.'),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        label=gettext_lazy('Username'),
        widget=forms.TextInput(attrs={'placeholder': gettext_lazy('Username'), 'class': 'mb-3'}),
    )
    password = forms.CharField(
        label=gettext_lazy('Password'),
        widget=forms.PasswordInput(attrs={'placeholder': gettext_lazy('Password')}),
        validators=[MinLengthValidator(3)],
    )