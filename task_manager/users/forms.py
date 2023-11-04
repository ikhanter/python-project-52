from django import forms
from .models import CustomUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy


class UsersCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label=gettext_lazy('Password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': gettext_lazy('Password')
            },
        ),
        validators=[MinLengthValidator(3)],
        help_text=gettext_lazy('Your password must contain at least 3 symbols.')
    )
    password2 = forms.CharField(
        label=gettext_lazy('Confirm password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': gettext_lazy('Confirm password'),
            }
        ),
        validators=[MinLengthValidator(3)],
        help_text=gettext_lazy('For the password confirmation, please, enter the password one more time.'))  # noqa: E501

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': gettext_lazy('First name'),
            'last_name': gettext_lazy('Last name'),
            'username': gettext_lazy('Username'),
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': gettext_lazy('First name'),
                    'class': 'mb-3'
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': gettext_lazy('Last name'),
                    'class': 'mb-3'
                },
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': gettext_lazy('Username'),
                    'class': 'mb-3'
                }
            ),
        }
        help_texts = {
            'username': gettext_lazy('Required field. Max length is 150 symbols. Letters, digits and  @/./+/-/_ symbols are allowed.'),  # noqa: E501
        }

    def clean_password(self):
        password1 = self.data['password1']
        password2 = self.data['password2']
        if password1 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
