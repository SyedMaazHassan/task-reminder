from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .forms import *
from django.core.serializers import serialize
from django.template.loader import render_to_string
from django.template import RequestContext



# main page function

def index(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("login")

    context['allreminders'] = reminder.objects.filter(added_by = request.user).order_by("-id")
    temp = []

    for i in context['allreminders']:
        temp_dict = {
            "type": 'Feature',
            "geometry": {
                "type": 'Point',
                "coordinates": [i.service_installation_place.lang, i.service_installation_place.lat]
            },
            "properties": {
                "id": i.id,
                # "title": '{{place.place_name}}',
                # "description": '{{place.place_description}}',
                # "image": '{{place.place_image}}',
                # "type": '{{place.place_type}}'
            }
        }

        temp.append(temp_dict)

    context['json_data'] = json.dumps(temp)

    # return render(request, "abc.html", context)
    return render(request, "all_markers.html", context)



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


def formsview(request, **kwargs):
    if not request.user.is_authenticated:
        return redirect("index")

    ctx = {
        'userform': CustomerForm, 
        'service_type': ServiceTypeForm, 
        'reminderform': ReminderForm,
        'services': Service_type.objects.all()
    }


    if request.method == 'POST':

        service_id = request.POST['selected_type'].split("-")[0]
        
        # type object of the system selected by the user
        selected_type = Service_type.objects.get(id = int(service_id)) #selected service
        
        # initializing service place as empty
        service_installation_place = ""

        # checking if user selected any place
        if 'is_place' in request.POST and request.POST['is_place'] == "on":
            latitude = request.POST['lat']
            langitude = request.POST['lang']

            # adding place in database
            # overwrite the "service_installation_place" variable
            service_installation_place = place.objects.create(lat = latitude, lang = langitude)

        # creating separate object of the user and save in database
        customer_info = CustomerInfo.objects.create(
            customer_name = request.POST['customer_name'],
            customer_email = request.POST['customer_email'],
            customer_address = request.POST['customer_address'],
            organization_number = request.POST['organization_number'],
            qr_code = request.POST['qr_code']
        ) 

        # checking if user wants to be reminded
        is_remind = request.POST['allEmails'] != ""

        # creating reminder object from the given information
        new_reminder = reminder.objects.create(
            installation_date = request.POST['installation_date'],
            next_service_date = request.POST['next_service_date'],
            service_installation_place = service_installation_place,
            service_type = selected_type,
            is_remind = is_remind,
            customer = customer_info,
            reminder_email = request.POST['allEmails'],
            added_by = request.user
        )

        return redirect('index')

    return render(request, 'main.html', ctx)
    # html = render_to_string('main.html', ctx, RequestContext(request))
    # return JsonResponse(html)

# def mainview(request):
#     # qs = Geoinfo.objects.filter(reminder=True)
#     # print(qs[0].reminder)
#     return render(request,'all_markers.html')

