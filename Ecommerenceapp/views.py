from django.shortcuts import render, redirect
from .models import *
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car = Car.objects.order_by('-created_date')
    search_model = Car.objects.values_list('model',flat=True).distinct()
    search_city = Car.objects.values_list('city',flat=True).distinct()
    search_year = Car.objects.values_list('year',flat=True).distinct()
    search_body_style = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'teams': teams,
        "featured_cars":featured_cars,
        "all_car":all_car,
        "search_model":search_model,
        "search_city":search_city,
        'search_year':search_year,
        'search_body_style':search_body_style



    }
    return render(request , 'pages/home.html', data)



def abouts(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams,
    }
    return render(request , 'pages/abouts.html',data)

def services(request):
    return render(request , 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        Phone = request.POST['phone']
        message =  request.POST['message']
        email_subject = 'You have a new message from Carzone website regarding '+ subject
        message_body = 'Name: '+ name + '\n Email: '+ email + '\n Phone: ' + Phone + '\n  Message ' + message

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'sherlockrai@gmail.com',
            [admin_email],
            fail_silently=False
            )
        messages.success(request , 'Thank You for contacting us , We will get back to you  shortly')
        return redirect('contact')
    return render(request , 'pages/contact.html')
