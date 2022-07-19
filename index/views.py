from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .models import WhatsNew, WhatWeDo, CustomersReview
from django.conf import settings

# Create your views here.
def index(request):
    news = WhatsNew.objects.all()
    activities = WhatWeDo.objects.all()
    reviews = CustomersReview.objects.all()
    context = {'news': news, 'activities': activities, 'reviews': reviews}
    return render(request, 'index/index.html', context)

def about(request):
    return render(request, 'index/about.html')

def contact(request):
    if request.method == 'POST':
        
        subject = request.POST['subject'],

        body = {
            'name':request.POST['name'],
            'email':request.POST['email_address'],
            'category':request.POST['category'],
            'message':request.POST['message'],
        }

        msg = "\n".join(body.values())

        try:
            send_mail(
                subject, 
                msg,
                settings.EMAIL_HOST_USER,
                ['asimieanicholas@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully...')

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect ("index:contact")
    return render(request, "index/contact.html")