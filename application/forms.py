from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = '__all__'


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = Service_type
        exclude = ['customer','pin_color' ]


class ReminderForm(forms.ModelForm):
    class Meta:
        model = reminder
        exclude = ['service_type', 'customer', 'service_installation_place', 'reminder_email', 'is_remind', 'added_by']
