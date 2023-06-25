from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from django.core.mail import send_mail


from django.shortcuts import render
from core.emailform import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def contact(request):
    form = ContactMeForm()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)
            subject = "Contact form inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email': form.cleaned_data['emailid'],
                'phonenumber': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            sender = form.cleaned_data['emailid']
            recipient = ['gameforyash@gmail.com']
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Your respoce has been submited successfully")
    context = {
        'form':form,
    }
    return render(request, "core/contact.html", context)

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

# def contact(request):
#     emailSubject = "Hi, " + (request.user) 
#     EmailBody=""
#     senderEmail="order@example.com"
#     receiverEmail = (request.user.email)
#     send_mail(emailSubject, EmailBody, senderEmail, [receiverEmail], fail_silently=False)
#     #send_mail('subject', 'body of the message', 'sender@example.com', ['receiver@example.com'], fail_silently=False)
#     return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

