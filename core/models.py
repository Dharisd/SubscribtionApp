from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    
    def __str__(self):
        return(f"{self.name} {self.phone_number}")




class SubscribtionService(models.Model):
    name = models.CharField(max_length=255)
    billing_cycle = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2,default=0)
    subscribers = models.ManyToManyField(
        Subscriber,
        null=True,
        blank=True,
    )

    ##adds a subscriber to a service given an instance of user
    def add_subscriber(subscriber_instance,self):
        self.subscribers.add(subscriber_instance)
        #create the subscribtion instance
        try:
            new_subscribtion = Subscribtion(subscriber=subscriber,service=self)
            new_subscribtion.save()
        except:
            #when the defined subscribtion object already exists
            return False
        
        return True
            




    def __str__(self):
        return (f"{self.name}")


class Subscribtion(models.Model):
    subscriber = models.ForeignKey(
        Subscriber,
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        SubscribtionService,
        on_delete=models.CASCADE,
    )
    started_at = models.DateField(
        null=True,
        blank=True
    )
    cancelled_at = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return(f"{self.subscriber.name} {self.service.name}")

    class Meta:
        unique_together = [
            'subscriber',
            'service',
            ]
