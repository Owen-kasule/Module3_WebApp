"""
URL configuration for bookings app.

Routes:
- / : Home page with booking form
- /booking/success/ : Booking confirmation page
- /admin/login/ : Admin login
- /admin/logout/ : Admin logout
- /admin/dashboard/ : Admin booking management
- /admin/bookings/<id>/cancel/ : Cancel a booking
- /admin/bookings/<id>/confirm/ : Confirm a booking
"""

from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('booking/success/', views.booking_success, name='booking_success'),
    
    # Admin authentication
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    
    # Admin dashboard
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Admin actions on bookings
    path('admin/bookings/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('admin/bookings/<int:booking_id>/confirm/', views.confirm_booking, name='confirm_booking'),
]
