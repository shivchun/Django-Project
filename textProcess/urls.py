from django.urls import path
from  textProcess import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('analyze/', views.analyze_view, name = 'analyze'),
]
