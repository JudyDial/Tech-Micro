# myapp/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

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

        # You can customize the success response message here
        response_data = {'message': 'Your message has been sent. Thank you!'}
        return JsonResponse(response_data)
    else:
        # Handle GET request if needed
        return JsonResponse({'error': 'Invalid request method'}, status=400)