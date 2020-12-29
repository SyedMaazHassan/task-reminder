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


class GeoInfoForm(forms.ModelForm):
    class Meta:
        model = Geoinfo
        exclude = ['service_type', 'customer']
