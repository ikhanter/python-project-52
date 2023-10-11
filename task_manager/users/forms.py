from django import forms
from .models import CustomUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy


class UsersCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': gettext_lazy('Confirm password')}),
        validators=[MinLengthValidator(3)],
        help_text=gettext_lazy('For the password confirmation, please, enter the password one more time.'))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password']
        labels = {
            'first_name': gettext_lazy('First name'),
            'last_name': gettext_lazy('Last name'),
            'username': gettext_lazy('Username'),
            'password': gettext_lazy('Password'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': gettext_lazy('First name'), 'class': 'mb-3'}),
            'last_name': forms.TextInput(attrs={'placeholder': gettext_lazy('Last name'), 'class': 'mb-3'}),
            'username': forms.TextInput(attrs={'placeholder': gettext_lazy('Username'), 'class': 'mb-3'}),
            'password': forms.PasswordInput(attrs={'placeholder': gettext_lazy('Password')}),
        }
        help_texts = {
            'username': gettext_lazy('Required field. Max length is 150 symbols. Letters, digits and  @/./+/-/_ symbols are allowed.'),
            'password': gettext_lazy('Your password must contain at least 3 symbols.'),
        }
