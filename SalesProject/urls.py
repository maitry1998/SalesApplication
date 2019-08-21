from django.contrib import admin
from django.urls import path, include
from SalesProject import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('signup/', views.signup, name='signup'),
    path('',views.index, name= "sell"),
    path('',views.index, name= "purchase"),
]
