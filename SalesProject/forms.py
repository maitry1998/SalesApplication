from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from SalesProject.models import Dealer


class SignUpForm(UserCreationForm):

    class Meta:
        model = Dealer
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','contact','address')