from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth


# Create your models here.

class CustomerInfo(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    customer_address = models.TextField()
    organization_number = models.IntegerField()
    qrcode = models.IntegerField(blank=True,default=0,null=True)
    contact_person_email = models.EmailField()
    reminder_email = models.EmailField()

    def __str__(self):
        return self.email


class Service_type(models.Model):
    choices = [('Purple', 'Alarm System'), ('Blue', 'Locking System')
        , ('Dark Purple', 'Door automation'), ('Black', 'Dim generator'),
               ('Green', 'Backup battery'),('Orange','Access control system')]
    color_choices = [('Backup battery', 'Green'), ('Locking System', 'Blue'), ('Dim generator', 'Black'), ('Alarm System', 'Purple'),
                     ('Access control system', 'Orange'),('Door automation','Dark Purple')]
    system_name = models.CharField(max_length=50, choices=color_choices)

    pin_color = models.CharField(max_length=50,choices=color_choices)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.system_name} with code {self.pin_color}'


class Geoinfo(models.Model):
    installation_date = models.DateTimeField()
    next_service_date = models.DateTimeField()
    service_installation_place = models.TextField()
    service_type = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    reminder = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.service_type.system_name} location {self.service_installation_place}'