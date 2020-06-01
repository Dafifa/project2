"""project2-->page1 URL Configuration

"""
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('',homePageView,name='home'),
]
