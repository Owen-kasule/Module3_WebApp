# Overview

I am building a production-ready booking management system to sharpen my full-stack skills. The goal is to modernize SoundHire’s rental business with an online experience for customers and a secure workflow for administrators, while gaining deeper practice with Django, cloud databases, and session-based authentication.

The SoundHire web app is a Django project backed by a Supabase PostgreSQL database. It loads equipment packages (Basic, Standard, Premium) with live pricing, accepts booking requests through validated forms, and provides an admin dashboard for reviewing, filtering, and updating reservation statuses.

**Run the development server**
```bash
cd "/home/kasule/Documents/2025 Semester Winter/CSE 310: Applied Programming/SoundHire/Module3_WebApp"
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

**Software Demo Video:** [Software Demo Video](https://youtube.com/PLACEHOLDER)

# Web Pages

- **Homepage (`/`)**: Lists all packages pulled from Supabase and shows a booking form that validates inputs, calculates totals, and posts new bookings. Successful submissions transition to the booking success page.
- **Booking Success (`/booking-success/`)**: Confirms receipt of the request, echoes the customer name, and links back to the homepage.
- **Admin Login (`/admin/login/`)**: Access-code gate backed by environment variables; on success, redirects to the admin dashboard; failed attempts show inline errors.
- **Admin Dashboard (`/admin/dashboard/`)**: Session-protected view with booking stats (counts and revenue), status filtering, search, and action buttons to confirm or cancel bookings. Logout returns the user to the login screen.

# Development Environment

- Django 5.2.9, Python 3.14
- Supabase Python client 2.24.0 with PostgreSQL 15 backend
- Bootstrap 5.3 for responsive UI
- python-dotenv for environment management
- Git 2.43+ on Ubuntu 22.04 and VS Code for development

# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/)
- [Supabase Python Docs](https://supabase.com/docs/reference/python/introduction)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

# Future Work

- Add customer accounts with secure login and profile management
- Send email/SMS notifications for booking updates
- Integrate payments (Stripe/PayPal) and generate PDF invoices
- Build a real-time availability calendar and booking history
- Expand admin tools (bulk actions, exports, and advanced analytics)
