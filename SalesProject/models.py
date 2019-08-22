from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class Dealer(User):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #email = models.EmailField(max_length=254)
    contact=models.IntegerField()
    address=models.CharField(max_length=50)

class Item(models.Model):
    seller=models.ForeignKey(Dealer,related_name="SellDealer",on_delete=models.CASCADE)
    buyer=models.ForeignKey(Dealer,related_name="BuyDealer",on_delete=models.CASCADE, null=True)
    ItemName=models.CharField(max_length=50)
    ItemPrice=models.DecimalField(decimal_places=2,max_digits=8)
    ItemImage=models.ImageField(upload_to='images/')
    ItemDescription= models.TextField()


