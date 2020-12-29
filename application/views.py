from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .forms import *
from django.core.serializers import serialize


# main page function

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return redirect('index')


# function for signup

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        org_name = ""

        if 'org_name' in request.POST and request.POST['org_name'] != "":
            org_name = request.POST['org_name']

        context = {
            "name": name,
            "l_name": l_name,
            "email": email,
            "pass1": pass1,
            "pass2": pass2,
            "org_name": org_name
        }
        if pass1 == pass2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "email"
                return render(request, "signup.html", context)

            # email = organization name

            user = User.objects.create_user(username=email, email=org_name, first_name=name, password=pass1,
                                            last_name=l_name)
            user.save()

            return redirect("login")
        else:
            messages.info(request, "Your pasword doesn't match!")
            context['border'] = "password"
            return render(request, "signup.html", context)

    return render(request, "signup.html")


# function for login

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'email': email,
            'password': password
        }
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Incorrect login details!")
            return render(request, "login.html", context)
            # return redirect("login")
    else:
        return render(request, "login.html")


# function for logout

def logout(request):
    auth.logout(request)
    return redirect("index")


# form to make a service reminder

def formsview(request, **kwargs):
    ctx = {'userform': CustomerForm, 'service_type': ServiceTypeForm, 'geoInfo': GeoInfoForm}
    if request.method == 'POST':
        reminder = False

        # checking if the reminder is true or not
        try:
            if request.POST['reminder'] == 'on':
                reminder = True
        except:
            pass

        # creating the customer object
        customer_info = CustomerInfo.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            organization_number=request.POST['organization_number'],
            customer_address=request.POST['customer_address'],
            contact_person_email=request.POST['contact_person_email'],
            reminder_email=request.POST['reminder_email']
        )

        # getting the service type
        service_type = Service_type.objects.get(system_name=request.POST['system_name'])

        # creating the reminder and geoinfo object based on the previous instances
        geo_info = Geoinfo.objects.create(
            service_type=service_type,
            installation_date=request.POST['installation_date'],
            next_service_date=request.POST['next_service_date'],
            service_installation_place=request.POST['service_installation_place'],
            reminder=reminder,
            customer=customer_info
        )
        return redirect('main-view')

    return render(request, 'main.html', ctx)

# displaying reminders in card form
def mainview(request):
    qs = Geoinfo.objects.filter(reminder=True)
    return render(request, 'all_markers.html', {'qs': qs})
