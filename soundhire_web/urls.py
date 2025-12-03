"""
URL configuration for soundhire_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Keep Django admin separate from our custom admin
    path('', include('bookings.urls')),  # All booking-related URLs at root
]
