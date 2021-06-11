from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from core.models import Subscriber,Subscribtion,SubscribtionService
from django.views.generic.edit import CreateView




class ListSubscribtionServices(ListView):
    template_name = "core/list_services.html"
    context_object_name = "services"
    model = SubscribtionService


