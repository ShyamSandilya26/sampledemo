from django import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.addstudent,name='addstudent')
]