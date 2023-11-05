from django import forms
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy


class LoginForm(forms.Form):
    username = forms.CharField(
        label=gettext_lazy('Username'),
        widget=forms.TextInput(attrs={
            'placeholder': gettext_lazy('Username'),
            'class': 'mb-3'}
        ),
    )
    password = forms.CharField(
        label=gettext_lazy('Password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': gettext_lazy('Password')}
        ),
        validators=[MinLengthValidator(3)],
    )
