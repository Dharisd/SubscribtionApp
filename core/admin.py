from django.contrib import admin
from .models import Subscribtion,SubscribtionService,Subscriber
# Register your models here.



#set council branding
admin.site.site_title = "Subscribtion Admin"
admin.site.site_header = "Subscribtion Dashboard"
admin.site.index_title = "Dashboard"


# Register your models here.




@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number")


@admin.register(Subscribtion)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display = ("subscriber","service")

@admin.register(SubscribtionService)
class SubscribtionServiceAdmin(admin.ModelAdmin):
    list_display = ("name","billing_cycle")



