from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic

from SalesProject.forms import SignUpForm, SellingForm
from SalesProject.models import Item, Dealer


def index(request):
    return render(request, "index.html")

def individual(request,eid):
    item=Item.objects.get(id=eid)
    context={
        'item' : item ,
    }
    return render(request, "individual.html",context)


def sell(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SellingForm(request.POST, files=request.FILES)
            #import ipdb;ipdb.set_trace()
            if form.is_valid():
                form.save()
                item = Item.objects.all()
                context = {
                    'item': item
                }
                return render(request, 'Items.html', context)
        else:
            form = SellingForm(initial={'seller':Dealer.objects.get(id=request.user.id)})
        return render(request, 'Selling.html', {'form': form})
    else:
        return redirect('login')

def purchase(request):
    return render(request, "buying.html")

def items(request):
    if request.user.is_authenticated:
        item = Item.objects.all()
        context = {
            'item': item
        }
        return render(request, "Items.html",context)
    else:
        return redirect('login')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})