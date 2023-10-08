# myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='portfolio-details'),
   path('contact/', views.contact_form, name='contact_form'),

    # Add more URL patterns for other pages
]
