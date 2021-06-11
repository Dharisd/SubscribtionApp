from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from core.models import Subscriber,Subscribtion,SubscribtionService
from django.views.generic.edit import CreateView


class CreateSubscriberView(CreateView):
    template_name = "core/create_subscribers.html"
    fields = ["name","phone_number"]
    model = Subscriber
    success_url = reverse_lazy('subscribtion-app:list-subscribers')




class ListSubscribersView(ListView):
    template_name = "core/list_subscribers.html"
    context_object_name = "subscribers"
    model = Subscriber