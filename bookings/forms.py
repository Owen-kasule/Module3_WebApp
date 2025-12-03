"""
Django forms for SoundHire bookings application.

Contains forms for:
- Customer booking submission
- Admin login/authentication
"""

from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta


class BookingForm(forms.Form):
    """
    Form for customers to submit equipment rental bookings.
    
    Fields collect customer information, event details, and package selection.
    Package choices are dynamically populated from Supabase data.
    """
    
    customer_name = forms.CharField(
        max_length=200,
        label="Your Full Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
            'required': True
        })
    )
    
    customer_email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
            'required': True
        })
    )
    
    customer_phone = forms.CharField(
        max_length=20,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+256 XXX XXXXXX',
            'required': True
        })
    )
    
    event_date = forms.DateField(
        label="Event Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'required': True
        }),
        help_text="Select the date when you need the equipment"
    )
    
    package_id = forms.ChoiceField(
        label="Select Package",
        choices=[],  # Will be populated dynamically
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        })
    )
    
    include_dj = forms.BooleanField(
        required=False,
        label="Add Professional DJ Service",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        help_text="Check this box to include DJ service with your booking"
    )
    
    notes = forms.CharField(
        required=False,
        label="Additional Notes (Optional)",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Any special requirements or questions?'
        })
    )
    
    def clean_event_date(self):
        """
        Validate that event date is in the future.
        
        Returns:
            date: Validated event date
            
        Raises:
            ValidationError: If date is in the past
        """
        event_date = self.cleaned_data.get('event_date')
        
        if event_date:
            # Check if date is at least tomorrow (allow same-day bookings)
            min_date = date.today()
            
            if event_date < min_date:
                raise ValidationError(
                    "Event date cannot be in the past. Please select a future date."
                )
            
            # Optional: Check if date is too far in the future (e.g., 1 year)
            max_date = date.today() + timedelta(days=365)
            if event_date > max_date:
                raise ValidationError(
                    "Event date cannot be more than 1 year in the future."
                )
        
        return event_date
    
    @classmethod
    def from_packages(cls, packages: list[dict], dj_rate: float = 550000) -> "BookingForm":
        """
        Create a BookingForm with package choices populated from Supabase data.
        
        Args:
            packages: List of package dictionaries from Supabase
                     Each should have: id, name, daily_rate
            dj_rate: DJ daily rate (from settings table)
        
        Returns:
            BookingForm: Form instance with package_id choices populated
            
        Example:
            packages = fetch_packages()  # From supabase_client
            dj_rate = get_dj_rate()
            form = BookingForm.from_packages(packages, dj_rate)
        """
        form = cls()
        
        # Build choices as (value, label) tuples
        # Format: (package_id, "Package Name - UGX daily_rate (+UGX dj_rate for DJ)")
        choices = []
        for pkg in packages:
            pkg_id = pkg.get('id')
            pkg_name = pkg.get('name', 'Unknown')
            daily_rate = pkg.get('daily_rate', 0)
            
            # Format price with thousands separator
            daily_rate_formatted = f"{daily_rate:,.0f}"
            dj_fee_formatted = f"{dj_rate:,.0f}"
            
            # Build label
            label = f"{pkg_name} - UGX {daily_rate_formatted}"
            if dj_rate > 0:
                label += f" (+UGX {dj_fee_formatted} for DJ)"
            
            choices.append((str(pkg_id), label))
        
        # Update the package_id field choices
        form.fields['package_id'].choices = choices
        
        return form


class AdminLoginForm(forms.Form):
    """
    Simple form for admin authentication.
    
    Uses an access code (not username/password) for simplicity.
    The access code is stored in Django settings (loaded from .env).
    """
    
    access_code = forms.CharField(
        max_length=100,
        label="Admin Access Code",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter admin access code',
            'required': True
        }),
        help_text="Enter the admin access code to view and manage bookings"
    )
    
    def clean_access_code(self):
        """
        Validate that access code is not empty.
        
        Returns:
            str: Cleaned access code
        """
        code = self.cleaned_data.get('access_code', '').strip()
        
        if not code:
            raise ValidationError("Access code is required.")
        
        return code
