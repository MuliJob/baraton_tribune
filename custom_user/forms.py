"""Login and register form"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


# - Create/Register a user (Model Form)

class CreateUserForm(UserCreationForm):
    """Register form"""
    email = forms.EmailField(

    )

    password1 = forms.CharField(
    )

    password2 = forms.CharField(
    )

    class Meta:
        """Class meta"""
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        """Ensure email is unique"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email


# - Authenticate a user (Login Form)

class LoginForm(AuthenticationForm):
    """Login form (Customized)"""
    username = forms.EmailField(

    )
    password = forms.CharField(

    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            if not User.objects.filter(email=email).exists():
                self.add_error('username', _("No account found with this email address."))
                return self.cleaned_data

            user = authenticate(self.request, username=email, password=password)

            if user is None:
                self.add_error('password', _("Incorrect password. Please try again!"))
            elif not user.is_active:
                self.add_error('username', _("This account is inactive."))

        return self.cleaned_data
