from django.urls import path

#connects the views.py page and this page

from . import views

#url patterns for the two pages on mysite
urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
]