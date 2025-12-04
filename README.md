# Overview

I am building a production-ready booking management system to sharpen my full-stack skills. The goal is to modernize SoundHire's rental business with an online experience for customers and a secure workflow for administrators, while gaining deeper practice with Django, cloud databases, and session-based authentication. The app connects to Supabase to load packages, accept bookings, and manage reservation statuses through a simple admin interface.

**Run the development server**
```bash
cd "/home/kasule/Documents/2025 Semester Winter/CSE 310: Applied Programming/SoundHire/Module3_WebApp"
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

[Software Demo Video](https://youtu.be/LfzBtriuP0U)

# Web Pages

- **Homepage (`/`)**: Dynamically lists packages from Supabase and shows a booking form that validates inputs, calculates totals, and creates new bookings; successful submissions transition to the booking success page.
- **Booking Success (`/booking-success/`)**: Confirms receipt, shows the customer name, and links back to the homepage.
- **Admin Login (`/admin/login/`)**: Access-code gate driven by environment variables; on success, redirects to the admin dashboard; failed attempts display inline errors.
- **Admin Dashboard (`/admin/dashboard/`)**: Session-protected view with booking stats (counts and revenue), status filtering, search, and action buttons to confirm or cancel bookings; logout returns to the login page.

# Development Environment

- Tools: VS Code on Ubuntu 22.04 with Git 2.43+
- Language/Framework: Python 3.14, Django 5.2.9
- Libraries/Services: Supabase Python client 2.24.0 (PostgreSQL backend), Bootstrap 5.3, python-dotenv

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
