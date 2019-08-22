from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput

from SalesProject.models import Dealer, Item


class SignUpForm(UserCreationForm):

    class Meta:
        model = Dealer
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','contact','address')

class SellingForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('ItemName', 'ItemPrice', 'ItemImage', 'ItemDescription', 'seller')

        widgets = {'seller': HiddenInput()}


