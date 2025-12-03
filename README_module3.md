# Module 3: Django Web Application for SoundHire

## Overview

This is a Django web application that provides a user-friendly interface for the SoundHire sound equipment rental business. It integrates with the Supabase database created in Module 1 to manage bookings online.

## Features

### Public Features
- **Package Browsing**: View all available sound equipment packages with pricing
- **Online Booking**: Submit booking requests through an interactive web form
- **Booking Confirmation**: Receive instant confirmation after submitting a booking
- **Input Validation**: Client-side and server-side validation for all form fields

### Admin Features
- **Secure Admin Login**: Access code-protected admin dashboard
- **Booking Management**: View all bookings with filtering by status
- **Status Updates**: Confirm or cancel bookings with one click
- **Analytics Dashboard**: View summary statistics and total revenue
- **Search & Filter**: Filter bookings by status (all, pending, confirmed, cancelled)

## Technology Stack

- **Django 5.2.9**: Python web framework
- **Supabase 2.24.0**: Backend database and API
- **Bootstrap 5.3**: Responsive UI framework
- **Python 3.14**: Programming language
- **python-dotenv**: Environment variable management

## Project Structure

```
Cloud Database_Supabase/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (DO NOT COMMIT)
├── .env.example                # Example environment configuration
│
├── soundhire_web/              # Django project configuration
│   ├── __init__.py
│   ├── settings.py             # Django settings with Supabase config
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
└── bookings/                   # Django app for bookings
    ├── __init__.py
    ├── apps.py                 # App configuration
    ├── models.py               # (Empty - using Supabase)
    ├── views.py                # View functions (7 views)
    ├── urls.py                 # URL routing
    ├── forms.py                # Django forms (BookingForm, AdminLoginForm)
    ├── supabase_client.py      # Supabase database helper
    │
    ├── templates/bookings/     # HTML templates
    │   ├── base.html           # Base template with navigation
    │   ├── home.html           # Public homepage with booking form
    │   ├── booking_success.html# Booking confirmation page
    │   ├── admin_login.html    # Admin authentication
    │   └── admin_dashboard.html# Admin booking management
    │
    └── static/bookings/        # CSS and static files
        └── styles.css          # Custom styling
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file and fill in your Supabase credentials:

```bash
cp .env.example .env
```

Edit `.env` and add:
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_ANON_KEY`: Your Supabase anonymous key
- `ADMIN_ACCESS_CODE`: Your chosen admin access code (default: `soundhire-admin-2025`)

### 3. Run Database Migrations

```bash
python manage.py migrate
```

This sets up Django's internal database for sessions and admin functionality.

### 4. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage Guide

### For Customers

1. **Browse Packages**
   - Visit the homepage to see all available packages
   - View pricing for equipment and DJ services

2. **Submit a Booking**
   - Scroll to the booking form
   - Fill in your contact details
   - Select your event date and package
   - Choose whether to include DJ service
   - Add any special notes
   - Click "Submit Booking Request"

3. **Confirmation**
   - Receive instant confirmation
   - SoundHire team will contact you within 24 hours

### For Admins

1. **Login**
   - Navigate to `/admin/login/`
   - Enter the admin access code from `.env`

2. **View Dashboard**
   - See summary statistics (total bookings, pending, confirmed, revenue)
   - View all bookings in a table format

3. **Filter Bookings**
   - Use the status filter dropdown
   - Options: All, Pending, Confirmed, Cancelled

4. **Manage Bookings**
   - **Confirm**: Click the ✓ button for pending bookings
   - **Cancel**: Click the ✗ button for any booking
   - View customer contact information
   - See booking notes and details

5. **Logout**
   - Click "Logout" in the navigation bar

## Database Schema

The application uses two Supabase tables:

### `packages` Table
- `id` (primary key)
- `name` (e.g., "Basic", "Standard", "Premium")
- `description`
- `base_price` (in UGX)
- `dj_extra_fee` (in UGX)

### `bookings` Table
- `id` (primary key)
- `customer_name`
- `customer_email`
- `customer_phone`
- `event_date` (date)
- `package_id` (foreign key → packages.id)
- `package_name` (cached)
- `package_price` (in UGX)
- `dj_included` (boolean)
- `dj_fee` (in UGX)
- `status` ("pending", "confirmed", "cancelled")
- `notes` (optional text)

## Code Architecture

### Views (bookings/views.py)

1. **home()**: Public homepage with package listing and booking form
   - GET: Display form
   - POST: Process booking submission

2. **booking_success()**: Confirmation page after successful booking

3. **admin_login()**: Admin authentication
   - GET: Display login form
   - POST: Validate access code and create session

4. **admin_logout()**: Clear admin session

5. **admin_dashboard()**: Admin interface for managing bookings
   - Requires admin session
   - Supports status filtering
   - Shows summary statistics

6. **confirm_booking(booking_id)**: Update booking status to "confirmed"
   - Admin-only, POST request

7. **cancel_booking(booking_id)**: Update booking status to "cancelled"
   - Admin-only, POST request

### Forms (bookings/forms.py)

1. **BookingForm**: Customer booking submission
   - Fields: name, email, phone, event_date, package, DJ option, notes
   - Validation: Future dates, required fields, email format
   - Dynamic package choices from Supabase

2. **AdminLoginForm**: Simple access code authentication
   - Single field: access_code (password input)

### Supabase Client (bookings/supabase_client.py)

Helper functions for database operations:
- `get_supabase_client()`: Create Supabase client instance
- `fetch_packages()`: Get all packages
- `create_booking(data)`: Insert new booking
- `list_bookings(status_filter)`: Get bookings with optional filter
- `update_booking_status(booking_id, new_status)`: Change booking status
- `get_booking_by_id(booking_id)`: Get single booking

All functions include error handling and logging.

## Security Features

- ✅ CSRF protection on all forms
- ✅ Session-based admin authentication
- ✅ Environment variables for sensitive data
- ✅ Input validation and sanitization
- ✅ SQL injection protection (via Supabase)
- ✅ Access control on admin routes

## Testing Checklist

- [ ] Homepage loads with packages
- [ ] Booking form validation works
- [ ] Can submit a new booking
- [ ] Booking confirmation page displays
- [ ] Admin login with correct code
- [ ] Admin login rejects wrong code
- [ ] Dashboard shows all bookings
- [ ] Can filter bookings by status
- [ ] Can confirm a pending booking
- [ ] Can cancel a booking
- [ ] Admin logout clears session

## Troubleshooting

### "Couldn't import Django"
```bash
pip install django
```

### "Supabase credentials not configured"
Check that `.env` file exists and contains:
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`

### "No packages found"
1. Log into Supabase dashboard
2. Verify `packages` table exists
3. Add sample packages using SQL or Supabase UI

### Admin login not working
Check `ADMIN_ACCESS_CODE` in `.env` matches what you're entering

## Module Requirements Met

✅ **Two or more dynamic HTML pages**
- Home page (package listing + booking form)
- Booking success page
- Admin login page
- Admin dashboard

✅ **User input**
- Booking form (7 fields)
- Admin login form
- Status filter dropdown

✅ **Real database interaction**
- Fetch packages from Supabase
- Create bookings in Supabase
- List bookings with filtering
- Update booking status

✅ **Clean, commented code**
- All files have docstrings
- Functions have clear explanations
- Comments explain business logic

## Future Enhancements

- Email notifications to customers
- SMS confirmations
- Payment gateway integration
- Customer booking history
- Calendar view for admin
- Export bookings to Excel
- Real-time availability checking
- Customer reviews and ratings

---

**Author**: Owen Kasule  
**Course**: CSE 310 - Applied Programming  
**Module**: 3 - Web Applications  
**Date**: December 2025
