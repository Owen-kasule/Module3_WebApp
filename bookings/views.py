"""
Views for SoundHire bookings web application.

Handles:
- Public booking form and submission
- Admin authentication
- Admin dashboard for managing bookings
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import HttpRequest, HttpResponse

from .forms import BookingForm, AdminLoginForm
from .supabase_client import (
    fetch_packages,
    create_booking,
    list_bookings,
    update_booking_status,
    get_dj_rate
)


def home(request: HttpRequest) -> HttpResponse:
    """
    Public home page with package information and booking form.
    
    GET: Display packages and empty booking form
    POST: Process booking submission and redirect to success page
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered home.html template
    """
    # Fetch available packages and DJ rate from Supabase
    packages = fetch_packages()
    dj_rate = get_dj_rate()
    
    if request.method == 'POST':
        # Create form with POST data and package choices
        form = BookingForm(request.POST)
        form.fields['package_id'].choices = [
            (str(pkg['id']), pkg['name']) for pkg in packages
        ]
        
        if form.is_valid():
            # Extract form data
            customer_name = form.cleaned_data['customer_name']
            customer_email = form.cleaned_data['customer_email']
            customer_phone = form.cleaned_data['customer_phone']
            event_date = form.cleaned_data['event_date'].isoformat()
            package_id = int(form.cleaned_data['package_id'])
            include_dj = form.cleaned_data['include_dj']
            notes = form.cleaned_data.get('notes', '')
            
            # Find the selected package to get pricing details
            selected_package = next(
                (pkg for pkg in packages if pkg['id'] == package_id),
                None
            )
            
            if not selected_package:
                messages.error(request, "Invalid package selected. Please try again.")
                form = BookingForm.from_packages(packages, dj_rate)
            else:
                # Calculate pricing
                package_name = selected_package['name']
                package_price = selected_package['daily_rate']
                dj_fee = dj_rate if include_dj else 0
                total_price = package_price + dj_fee
                
                # Build booking payload for Supabase (matches original schema)
                booking_data = {
                    'customer_name': customer_name,
                    'email': customer_email,
                    'phone': customer_phone,
                    'start_date': event_date,
                    'end_date': event_date,  # Single day event
                    'package_id': package_id,
                    'qty': 1,  # Single package rental
                    'include_dj': include_dj,
                    'total_price': total_price,
                    'status': 'pending'  # New bookings start as pending
                }
                
                # Create booking in Supabase
                result = create_booking(booking_data)
                
                if result:
                    # Success - store booking ID and redirect
                    request.session['last_booking_name'] = customer_name
                    request.session['last_booking_package'] = package_name
                    messages.success(
                        request,
                        f"Booking submitted successfully! We'll contact you at {customer_email}"
                    )
                    return redirect('booking_success')
                else:
                    # Error creating booking
                    messages.error(
                        request,
                        "Sorry, there was an error processing your booking. Please try again."
                    )
                    form = BookingForm.from_packages(packages, dj_rate)
        else:
            # Form validation failed - errors will be displayed in template
            pass
    else:
        # GET request - display empty form
        form = BookingForm.from_packages(packages, dj_rate)
    
    context = {
        'packages': packages,
        'form': form,
        'dj_rate': dj_rate
    }
    
    return render(request, 'bookings/home.html', context)


def booking_success(request: HttpRequest) -> HttpResponse:
    """
    Success page displayed after booking submission.
    
    Shows a thank you message with booking details from session.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered booking_success.html template
    """
    # Retrieve booking details from session (if available)
    customer_name = request.session.get('last_booking_name', 'Customer')
    package_name = request.session.get('last_booking_package', 'your selected package')
    
    # Clear session data after displaying (one-time use)
    if 'last_booking_name' in request.session:
        del request.session['last_booking_name']
    if 'last_booking_package' in request.session:
        del request.session['last_booking_package']
    
    context = {
        'customer_name': customer_name,
        'package_name': package_name
    }
    
    return render(request, 'bookings/booking_success.html', context)


def admin_login(request: HttpRequest) -> HttpResponse:
    """
    Admin login page using simple access code authentication.
    
    GET: Display login form
    POST: Validate access code and redirect to dashboard
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered admin_login.html template or redirect
    """
    # If already logged in, redirect to dashboard
    if request.session.get('is_soundhire_admin'):
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        
        if form.is_valid():
            access_code = form.cleaned_data['access_code']
            
            # Check if access code matches the configured admin code
            if access_code == settings.ADMIN_ACCESS_CODE:
                # Set session flag for admin access
                request.session['is_soundhire_admin'] = True
                messages.success(request, "Successfully logged in as admin")
                return redirect('admin_dashboard')
            else:
                # Invalid access code
                messages.error(request, "Invalid access code. Please try again.")
                form = AdminLoginForm()
    else:
        # GET request - display empty form
        form = AdminLoginForm()
    
    context = {'form': form}
    return render(request, 'bookings/admin_login.html', context)


def admin_logout(request: HttpRequest) -> HttpResponse:
    """
    Log out admin user by clearing session flag.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Redirect to home page
    """
    if 'is_soundhire_admin' in request.session:
        del request.session['is_soundhire_admin']
    
    messages.success(request, "Successfully logged out")
    return redirect('home')


def admin_dashboard(request: HttpRequest) -> HttpResponse:
    """
    Admin dashboard for viewing and managing bookings.
    
    Requires admin authentication (session flag).
    Supports filtering by booking status via query parameter.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered admin_dashboard.html template or redirect
    """
    # Check if user is logged in as admin
    if not request.session.get('is_soundhire_admin'):
        messages.warning(request, "Please log in to access the admin dashboard")
        return redirect('admin_login')
    
    # Get status filter from query parameters
    status_filter = request.GET.get('status', 'all')
    
    # Validate status filter
    valid_statuses = ['all', 'pending', 'confirmed', 'cancelled']
    if status_filter not in valid_statuses:
        status_filter = 'all'
    
    # Fetch bookings and packages from Supabase
    filter_param = None if status_filter == 'all' else status_filter
    bookings = list_bookings(status_filter=filter_param)
    packages = fetch_packages()
    dj_rate = get_dj_rate()
    
    # Create package lookup for enriching booking data
    package_lookup = {pkg['id']: pkg for pkg in packages}
    
    # Enrich bookings with package info and computed fields
    for booking in bookings:
        package_id = booking.get('package_id')
        if package_id and package_id in package_lookup:
            pkg = package_lookup[package_id]
            booking['package_name'] = pkg['name']
            booking['package_price'] = pkg['daily_rate']
            booking['dj_fee'] = dj_rate if booking.get('include_dj') else 0
            booking['customer_email'] = booking.get('email', '')
            booking['customer_phone'] = booking.get('phone', '')
            booking['event_date'] = booking.get('start_date', '')
            booking['dj_included'] = booking.get('include_dj', False)
    
    # Calculate summary statistics
    total_bookings = len(bookings)
    pending_count = sum(1 for b in bookings if b.get('status') == 'pending')
    confirmed_count = sum(1 for b in bookings if b.get('status') == 'confirmed')
    cancelled_count = sum(1 for b in bookings if b.get('status') == 'cancelled')
    
    # Calculate total revenue from confirmed bookings
    total_revenue = sum(
        b.get('total_price', 0)
        for b in bookings
        if b.get('status') == 'confirmed'
    )
    
    context = {
        'bookings': bookings,
        'current_filter': status_filter,
        'total_bookings': total_bookings,
        'pending_count': pending_count,
        'confirmed_count': confirmed_count,
        'cancelled_count': cancelled_count,
        'total_revenue': total_revenue
    }
    
    return render(request, 'bookings/admin_dashboard.html', context)


def cancel_booking(request: HttpRequest, booking_id: int) -> HttpResponse:
    """
    Cancel a booking by updating its status to 'cancelled'.
    
    Admin-only action. Requires POST request for security.
    
    Args:
        request: HTTP request object
        booking_id: ID of the booking to cancel
        
    Returns:
        HttpResponse: Redirect to admin dashboard
    """
    # Check if user is logged in as admin
    if not request.session.get('is_soundhire_admin'):
        messages.error(request, "Unauthorized access")
        return redirect('admin_login')
    
    # Only allow POST requests for this action
    if request.method != 'POST':
        messages.error(request, "Invalid request method")
        return redirect('admin_dashboard')
    
    # Update booking status in Supabase
    result = update_booking_status(booking_id, 'cancelled')
    
    if result:
        messages.success(
            request,
            f"Booking #{booking_id} has been cancelled successfully"
        )
    else:
        messages.error(
            request,
            f"Failed to cancel booking #{booking_id}. Please try again."
        )
    
    # Redirect back to dashboard, preserving status filter if present
    status_filter = request.GET.get('status', 'all')
    return redirect(f"/admin/dashboard/?status={status_filter}")


def confirm_booking(request: HttpRequest, booking_id: int) -> HttpResponse:
    """
    Confirm a booking by updating its status to 'confirmed'.
    
    Admin-only action. Requires POST request for security.
    
    Args:
        request: HTTP request object
        booking_id: ID of the booking to confirm
        
    Returns:
        HttpResponse: Redirect to admin dashboard
    """
    # Check if user is logged in as admin
    if not request.session.get('is_soundhire_admin'):
        messages.error(request, "Unauthorized access")
        return redirect('admin_login')
    
    # Only allow POST requests for this action
    if request.method != 'POST':
        messages.error(request, "Invalid request method")
        return redirect('admin_dashboard')
    
    # Update booking status in Supabase
    result = update_booking_status(booking_id, 'confirmed')
    
    if result:
        messages.success(
            request,
            f"Booking #{booking_id} has been confirmed successfully"
        )
    else:
        messages.error(
            request,
            f"Failed to confirm booking #{booking_id}. Please try again."
        )
    
    # Redirect back to dashboard, preserving status filter if present
    status_filter = request.GET.get('status', 'all')
    return redirect(f"/admin/dashboard/?status={status_filter}")
