from django.shortcuts import render

# Create your views here.

def home(request):
    return  render(request,"homeApp/home.html")

def about(request):
    return  render(request,"homeApp/about.html")
