# Module 3: Django Web Application Setup Guide

This folder contains a complete, self-contained Django web application for the SoundHire equipment rental booking system.

## 📁 Folder Contents

```
Module3_WebApp/
├── bookings/                    # Main Django app with views, forms, templates
│   ├── views.py                # 7 view functions for web pages
│   ├── forms.py                # Booking and admin login forms
│   ├── models.py               # (Not used - using Supabase directly)
│   ├── supabase_client.py      # Database interaction functions
│   ├── templates/              # HTML templates
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── booking_success.html
│   │       ├── admin_login.html
│   │       └── admin_dashboard.html
│   └── static/                 # CSS stylesheets
│       └── bookings/
│           ├── styles.css      # Modern black & white design
│           └── styles_old.css  # Original design (backup)
├── soundhire_web/              # Django project settings
│   ├── settings.py            # Main configuration file
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI configuration
├── manage.py                   # Django management script
├── db.sqlite3                  # Local Django database (for sessions only)
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # Main project README
├── README_module3.md          # Technical documentation
├── QUICKSTART_MODULE3.md      # Quick start guide
└── MODULE3_COMPLETION_CHECKLIST.md  # Requirements verification
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Active Supabase account with database

### 2. Setup Instructions

```bash
# Navigate to the Module3_WebApp folder
cd Module3_WebApp

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp .env.example .env

# Edit .env file and add your Supabase credentials:
# SUPABASE_URL=your_supabase_url
# SUPABASE_ANON_KEY=your_anon_key
# ADMIN_ACCESS_CODE=soundhire-admin-2025
# DJANGO_SECRET_KEY=your-secret-key-here

# Run database migrations (for Django's internal tables only)
python manage.py migrate

# Start the development server
python manage.py runserver
```

### 3. Access the Application

- **Homepage**: http://127.0.0.1:8000/
- **Admin Login**: http://127.0.0.1:8000/admin/login/
- **Admin Code**: `soundhire-admin-2025` (stored in .env)

## 📊 Database Configuration

This application uses **Supabase** (PostgreSQL) as the primary database. The database contains:

- **packages** table: Equipment rental packages
- **bookings** table: Customer booking records
- **settings** table: System configuration (DJ rates, etc.)

The local `db.sqlite3` file is only used by Django for session management and internal tables.

## 🎨 Design Features

- Modern black, white, and grayscale color scheme
- Three package cards displayed in hero section with gradient backgrounds
- Fully responsive Bootstrap 5 layout
- Clean, professional typography with sharp edges
- Smooth hover animations and transitions

## 📝 Key Files Explained

### `bookings/supabase_client.py`
Contains 6 functions for database operations:
- `get_supabase_client()` - Initialize database connection
- `fetch_packages()` - Get all available packages
- `get_dj_rate()` - Get DJ service rate from settings
- `create_booking()` - Insert new booking
- `list_bookings()` - Retrieve bookings with filters
- `update_booking_status()` - Update booking status

### `bookings/views.py`
Contains 7 view functions:
- `home()` - Display packages and booking form
- `booking_success()` - Show confirmation page
- `admin_login()` - Admin authentication
- `admin_logout()` - Clear admin session
- `admin_dashboard()` - Manage bookings
- `confirm_booking()` - Confirm a booking
- `cancel_booking()` - Cancel a booking

### `bookings/forms.py`
- `BookingForm` - 7 input fields with validation
- `AdminLoginForm` - Access code authentication

## 🧪 Testing the Application

1. **Test Customer Booking Flow:**
   - Visit homepage
   - Fill out booking form
   - Submit and see success page

2. **Test Admin Dashboard:**
   - Go to `/admin/login/`
   - Enter access code: `soundhire-admin-2025`
   - View all bookings
   - Confirm or cancel bookings
   - Filter by status

## 📦 Dependencies

```
Django==5.2.9
supabase==2.24.0
python-dotenv==1.0.0
```

## 🔐 Security Notes

- Never commit `.env` file to Git (it's in `.gitignore`)
- Change `DJANGO_SECRET_KEY` in production
- Change `ADMIN_ACCESS_CODE` before deployment
- Use environment variables for all sensitive data

## 🌐 Deployment Considerations

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Add your domain to `ALLOWED_HOSTS` in `settings.py`
3. Use a production-grade WSGI server (Gunicorn, uWSGI)
4. Set up HTTPS with SSL certificates
5. Use a production database (PostgreSQL via Supabase)
6. Configure static file serving with WhiteNoise or CDN
7. Set strong, unique environment variables

## 📞 Support

For questions or issues:
- Check `README_module3.md` for technical details
- Review `QUICKSTART_MODULE3.md` for common solutions
- Verify requirements in `MODULE3_COMPLETION_CHECKLIST.md`

## ✅ Module 3 Requirements Met

- ✅ 4+ dynamic HTML pages
- ✅ User input forms with validation
- ✅ Real database interaction (Supabase)
- ✅ Clean, well-commented code
- ✅ Professional design and user experience

---

**Note**: This is a self-contained folder ready for Git submission. All necessary files are included.
