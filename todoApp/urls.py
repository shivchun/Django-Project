from django.urls import  path
from todoApp import  views

urlpatterns = [
    path('index/', views.index),
    path('add/', views.addTodo),
    path('complete/<int:id>/', views.complete),
    path('deleteCompleted/', views.deleteCompleted),
    path('deleteAll/', views.deleteAll),
]
