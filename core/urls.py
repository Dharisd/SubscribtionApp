from django.urls import path
from core.views.DashBoardViews import DashBoardView
from core.views.SubscriberViews import CreateSubscriberView,ListSubscribersView
from core.views.SubscribtionServiceViews import ListSubscribtionServices,DetailSubscribtionServicesView


app_name = "subscribtion-app"

urlpatterns = [
    path('dashboard', DashBoardView.as_view(), name='dashboard'),
    #all list views
    path('list/services', ListSubscribtionServices.as_view(), name='list-services'),
    path('list/subscribers', ListSubscribersView.as_view(), name='list-subscribers'),
    #create views
    path('create/subscribers', CreateSubscriberView.as_view(), name='create-subscribers'),

    #detail views
    path('details/<int:pk>', DetailSubscribtionServicesView.as_view(), name='detail-services'),



]