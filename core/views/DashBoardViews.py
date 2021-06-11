from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from core.models import Subscriber,Subscribtion,SubscribtionService
from django.views.generic.edit import CreateView


class DashBoardView(ListView):
    template_name = "core/dashboard.html"
    model = SubscribtionService
