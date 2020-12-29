from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth


# Create your models here.

class CustomerInfo(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    customer_address = models.TextField()
    organization_number = models.IntegerField()
    qrcode = models.IntegerField(blank=True, default=0, null=True)
    contact_person_email = models.EmailField()
    reminder_email = models.EmailField()

    def __str__(self):
        return self.email


class Service_type(models.Model):
    choices = [('Alarm System', 'Alarm System'), ('Locking System', 'Locking System')
        , ('Door automation', 'Door automation'), ('Dim generator', 'Dim generator'),
               ('Backup battery', 'Backup battery'), ('Access control system', 'Access control system')]
    color_choices = [('#2eff00', 'Green'),
                     ('#02baff', 'Blue'), ('#000000', 'Black'), ('#b36ae2', 'Purple'),
                     ('#ff9c34', 'Orange'), ('#8000ff', 'Dark Purple')]
    system_name = models.CharField(max_length=50, choices=choices)

    pin_color = models.CharField(max_length=50, choices=color_choices)

    def __str__(self):
        return f'{self.system_name} with code {self.pin_color}'


class Geoinfo(models.Model):
    installation_date = models.DateTimeField()
    next_service_date = models.DateTimeField()
    service_installation_place = models.TextField()
    service_type = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    reminder = models.BooleanField(default=False)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.service_type.system_name} location {self.service_installation_place}'
