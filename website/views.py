# myapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import smtplib
from email.message import EmailMessage
import logging

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create and save the Contact object
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send email with form data
        msg = EmailMessage()
        msg.set_content(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        # Set the sender and recipient email addresses
        msg['From'] = 'benjaminkaranja8393@gmail.com'
        msg['To'] = 'benjaminkaranja8393official@gmail.com'  # Replace with your recipient's email address
        msg['Subject'] = 'New contact form submission'
        
        logging.basicConfig(level=logging.DEBUG)  

        try:
            # Connect to the SMTP server and establish a TLS-encrypted connection
            with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server and port
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection

                # Log in to your email account
                server.login('benjaminkaranja8393@gmail.com','hivx tzan alxy wxfs')  # Replace with your email and app password

                # Send the email
                server.send_message(msg)

            # You can customize the success response message here
            response_data = {'message': 'Your message has been sent. Thank you!'}
            return JsonResponse(response_data)

        except Exception as e:
            # Handle exceptions, log errors, and provide an error response
            logging.error(f"Error sending email: {e}")
            return JsonResponse({'error': 'An error occurred while sending the email.'}, status=500)

    else:
        # Handle GET request if needed
        return JsonResponse({'error': 'Invalid request method'}, status=400)
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            # Attempt to create a new subscriber
            subscriber = Subscriber.objects.create(email=email)
            subscriber.save()
            return JsonResponse({'message': 'Subscription successful!'})
        except Exception as e:
            # Handle the case where the email is not unique (already subscribed)
            return JsonResponse({'error': 'Email address already subscribed.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    