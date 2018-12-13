# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView



def HomePageView(request):
	return HttpResponse("<h3> HI <h3>")


#linking the things in the templates folder to the urls
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'