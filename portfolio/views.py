from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Services
# Create your views here.

class HomeView(ListView):
    model = Services
    template_name = "portfolio/index.html"
    def get_context_data(self, *argd, **kwargs):
        service_menu = Services.objects.all()
        context = super(HomeView,self).get_context_data(*argd, **kwargs)
        context["service_menu"] = service_menu
        return context

class ServiceView(DetailView):
    model = Services
    template_name = "portfolio/service.html"
    def get_context_data(self, *argd, **kwargs):
        service_menu = Services.objects.all()
        context = super(ServiceView,self).get_context_data(*argd, **kwargs)
        context["service_menu"] = service_menu
        return context


