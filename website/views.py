from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'website/index.html')   

def home1 (request):
    return render(request, 'website/home1.html')

def home2 (request):
    return render(request, 'website/home2.html')

def home3 (request):
    return render(request, 'website/home3.html') 

def home4 (request):
    return render(request, 'website/home4.html')

def home5 (request):
    return render(request, 'website/home5.html')

def home6 (request):
    return render(request, 'website/home6.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data.get('phone_number', '')
            budget = form.cleaned_data.get('budget', '')
            file = form.cleaned_data.get('file', None)

            # Send email to admin
            send_mail(
                f"New message from {full_name} - {subject}",
                f"Message: {message}\n\nBudget: {budget}\nPhone: {phone_number}\n",
                settings.EMAIL_HOST_USER,
                ['your_email@gmail.com'],  # Replace with your email
                fail_silently=False,
            )

            # Send confirmation email to sender
            send_mail(
                "Message Sent Successfully",
                "Thank you for contacting us. We will get back to you soon.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return HttpResponse("Your message was sent successfully!")  # You can redirect to a success page
        else:
            return render(request, 'website/home.html', {'form': form})  

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})