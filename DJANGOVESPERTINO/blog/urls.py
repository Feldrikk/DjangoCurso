from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('about/', views.about),
]