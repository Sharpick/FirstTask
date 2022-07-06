from django.contrib import admin
from django.urls import path
from ArticleApp import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/<str:title>/<str:content>/', views.edit),
    path('archive/', views.archive),
    path('archive/<int:id>/', views.archive),
    path('archive/delete/<int:id>/', views.delete),
]
