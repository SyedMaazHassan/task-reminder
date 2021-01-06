from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth


# Create your models here.

class CustomerInfo(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.EmailField(unique=False)
    customer_address = models.TextField()
    organization_number = models.IntegerField()
    qr_code = models.IntegerField(blank=True, default=0, null=True)
    # contact_person_email = models.EmailField()
    # reminder_email = models.TextField()

    def __str__(self):
        return self.email


class Service_type(models.Model):
    system_name = models.CharField(max_length=50)
    pin_color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.system_name} with code {self.pin_color}'

class place(models.Model):
    lat = models.FloatField()
    lang = models.FloatField()
    

class reminder(models.Model):
    installation_date = models.DateTimeField()
    next_service_date = models.DateTimeField()
    service_installation_place = models.ForeignKey(place, on_delete = models.CASCADE, null = True, blank = True)
    service_type = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    is_remind = models.BooleanField(default=False)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    reminder_email = models.TextField(null = True, blank = True)
    added_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f'{self.service_type.system_name} location {self.service_installation_place}'
