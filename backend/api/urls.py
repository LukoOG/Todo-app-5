from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('', views.overview),
    path('list', views.list),
    path('detail/<str:pk>', views.detail),
    path('create', views.create),
    path('update/<str:pk>', views.update),
    path('delete/<str:pk>', views.delete),
    path('token', views.token)
]
