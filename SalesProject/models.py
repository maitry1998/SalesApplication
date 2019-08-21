from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class Dealer(User):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #email = models.EmailField(max_length=254)
    contact=models.IntegerField(max_length=10)
    address=models.CharField(max_length=50)
