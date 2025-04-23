import logging
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

# Set up logging
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    # Redirect all traffic to home1 as the main entry point
    return render(request, 'website/home1.html', {'use_default_body': True})   

def home1(request):
    return render(request, 'website/home1.html', {'use_default_body': True})

# Portfolio page without default body
def portfolio_page(request):
    return render(request, 'website/portfolio.html')

def contact_view(request):
    logger.debug("Contact view called with method: %s", request.method)
    
    if request.method == 'POST':
        logger.debug("Processing POST request with data: %s", request.POST)
        form = ContactForm(request.POST, request.FILES)
        
        if form.is_valid():
            logger.debug("Form is valid, processing data")
            # Form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data.get('phone_number', '')
            budget = form.cleaned_data.get('budget', '')
            file = form.cleaned_data.get('file', None)

            logger.info("Sending email from %s about %s", full_name, subject)
            
            try:
                # Send email to admin
                send_mail(
                    f"New message from {full_name} - {subject}",
                    f"Message: {message}\n\nBudget: {budget}\nPhone: {phone_number}\n",
                    settings.EMAIL_HOST_USER,
                    ['begati16@gmail.com'],  # Update with your email
                    fail_silently=False,
                )

                # Send confirmation email to sender
                send_mail(
                    "Message Sent Successfully",
                    "Thank you for contacting me. I will get back to you soon.",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                
                logger.info("Emails sent successfully")
                return HttpResponse("Your message was sent successfully!")
                
            except Exception as e:
                logger.error("Error sending email: %s", str(e))
                return HttpResponse(f"An error occurred: {str(e)}")
        else:
            logger.warning("Form validation failed: %s", form.errors)
            # Render the home1 template instead
            return render(request, 'website/home1.html', {'form': form, 'use_default_body': True})  

    else:
        logger.debug("Processing GET request, creating empty form")
        form = ContactForm()

    # Render the home1 template
    return render(request, 'website/home1.html', {'form': form, 'use_default_body': True})