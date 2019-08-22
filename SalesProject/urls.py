from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from SalesProject import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('signup/', views.signup, name='signup'),
    path('sell/',views.sell, name= "sell"),
    path('purchase/',views.purchase, name= "purchase"),
    path('items/',views.items, name= "items"),
    path('individual/<int:eid>/',views.individual, name= "individual"),
    #url(r'^individual/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', views.emp_detail, name='emp_detail'),
]
