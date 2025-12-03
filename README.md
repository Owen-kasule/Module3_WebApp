# SoundHire Web Application

## Overview

As a software engineer, I wanted to deepen my understanding of full-stack web development by building a production-ready booking management system. This project transforms SoundHire's equipment rental business from manual operations into a modern web-based platform where customers can browse packages and submit bookings online, while administrators manage reservations through a secure dashboard. I chose this project to learn how to integrate Django with cloud databases, implement user authentication, and create responsive interfaces that serve both public customers and internal staff.

The SoundHire web application is a Django-based booking system that connects to a Supabase PostgreSQL database. The system displays three equipment packages (Basic, Standard, and Premium) with dynamic pricing pulled from the database, allows customers to submit booking requests through a validated form, and provides administrators with a dashboard to view, filter, and manage all bookings in real-time.

**To start the application:**
```bash
cd "/home/kasule/Documents/2025 Semester Winter/CSE 310: Applied Programming/SoundHire/Cloud Database_Supabase"
python manage.py runserver
```
Then visit: **http://127.0.0.1:8000/**

## Software Demo Video

[Software Demo Video](https://youtube.com/PLACEHOLDER)

## Web Pages

The application consists of four main web pages with intuitive navigation:

### 1. Homepage (`/`)
The landing page displays all equipment packages dynamically loaded from the Supabase database. Each package shows its name, description, and daily rate in Ugandan Shillings (UGX). A prominent booking form collects customer information including name, email, phone number, package selection, rental dates, quantity needed, and whether DJ services are required. When the user submits the form, Django validates all inputs server-side and calculates the total price based on rental duration, quantity, package rate, and optional DJ services.

**Transitions:** After successful form submission → Booking Success page

### 2. Booking Success (`/booking-success/`)
A confirmation page displays immediately after a customer submits a booking. It shows a success message with the customer's name and confirms that their booking request has been received with "pending" status. This page provides reassurance and clear instructions that an administrator will review the booking.

**Transitions:** "Return to Homepage" link → Homepage

### 3. Admin Login (`/admin/login/`)
A secure authentication page requiring an access code stored in environment variables (`ADMIN_ACCESS_CODE=soundhire-admin-2025`). The form validates the code server-side using Django sessions to maintain authenticated state. Invalid access code attempts display error messages.

**Transitions:** Successful login → Admin Dashboard

### 4. Admin Dashboard (`/admin/dashboard/`)
A protected management interface (requires authentication via session) showing comprehensive booking statistics including total bookings, confirmed count, pending count, cancelled count, and total revenue. The dashboard displays all bookings in a searchable table with filters for "all," "pending," "confirmed," and "cancelled" statuses. Each booking row shows customer details, package name (joined from the packages table), dates, quantities, DJ service status, total price, and current status. Administrators can confirm or cancel bookings with dedicated action buttons that trigger immediate status updates in the database.

**Transitions:** "Logout" button → Admin Login page

## Development Environment

- **Django 5.2.9** - Python web framework providing MVT (Model-View-Template) architecture, URL routing, form handling, and session management
- **Python 3.14** - Programming language with type hints and modern async capabilities
- **Supabase 2.24.0** - PostgreSQL cloud database platform with Python SDK for database operations
- **Bootstrap 5.3** - Frontend CSS framework for responsive design (via CDN)
- **python-dotenv 1.0.0** - Environment variable management for secure credential storage
- **Git 2.43+** - Version control system for tracking code changes
- **VS Code** - Integrated development environment with Python and Django extensions
- **PostgreSQL 15** - Relational database engine (hosted by Supabase)
- **Linux Ubuntu 22.04** - Development operating system

## Useful Websites

Resources that were instrumental in building this Django application:

- [Django Documentation](https://docs.djangoproject.com/) - Comprehensive guides on views, forms, templates, and URL routing
- [Supabase Python Documentation](https://supabase.com/docs/reference/python/introduction) - Python client library API reference and examples
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/) - Component library for responsive UI design
- [Django Form Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/) - Server-side validation patterns and custom validators
- [PostgreSQL Date Functions](https://www.postgresql.org/docs/current/functions-datetime.html) - SQL date operations for booking queries
- [MDN Web Docs](https://developer.mozilla.org/) - HTML5 form elements and semantic markup
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/) - Practical Django patterns and best practices

## Future Work

Planned enhancements to expand functionality and improve user experience:

- **User Authentication System** - Customer accounts with secure login, password reset, and profile management
- **Email Notifications** - Automated confirmation emails using SendGrid when bookings are confirmed or cancelled
- **Real-time Availability Calendar** - Interactive date picker showing unavailable dates based on current bookings and stock levels
- **Payment Integration** - Stripe or PayPal checkout flow for online payments with transaction records
- **Booking History** - Customer portal to view past and upcoming bookings with receipt downloads
- **Equipment Photo Gallery** - Image uploads for packages with carousel display and zoom functionality
- **Advanced Search & Filtering** - Filter packages by price range, features, and availability dates
- **Mobile Responsiveness** - Optimize UI for tablets and smartphones with touch-friendly controls
- **Revenue Analytics Dashboard** - Charts showing booking trends, popular packages, and revenue over time using Chart.js
- **SMS Notifications** - Text message confirmations via Twilio API integration
- **Customer Reviews** - Rating system and testimonials for completed bookings
- **Multi-language Support** - Internationalization (i18n) for English, Luganda, and Swahili
- **PDF Invoice Generation** - Downloadable booking invoices with company branding using ReportLab
- **Admin Bulk Operations** - Multi-select actions to confirm or cancel multiple bookings at once
- **Automated Testing** - Unit tests for views and forms, integration tests for database operations using pytest-django
