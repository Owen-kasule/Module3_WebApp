"""
Supabase client helper module for SoundHire bookings.

This module provides a wrapper around supabase-py to interact with
the Supabase database tables: packages and bookings.

All business data lives in Supabase (Module 1).
Django only handles web presentation and user interaction.
"""

from typing import List, Dict, Any, Optional
from supabase import create_client, Client
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def get_supabase_client() -> Client:
    """
    Create and return a Supabase client instance.
    
    Uses SUPABASE_URL and SUPABASE_ANON_KEY from Django settings,
    which are loaded from the .env file.
    
    Returns:
        Client: Configured Supabase client instance
        
    Raises:
        ValueError: If Supabase credentials are not configured
    """
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_ANON_KEY
    
    if not url or not key:
        raise ValueError(
            "Supabase credentials not configured. "
            "Please set SUPABASE_URL and SUPABASE_ANON_KEY in .env file."
        )
    
    return create_client(url, key)


def fetch_packages() -> List[Dict[str, Any]]:
    """
    Fetch all sound equipment packages from Supabase.
    
    Returns a list of packages with their details:
    - id: Package primary key
    - name: Package name (e.g., "Basic", "Standard", "Premium")
    - description: Package description
    - daily_rate: Daily rental rate in UGX
    - stock: Available inventory count
    
    Returns:
        List[Dict]: List of package dictionaries, empty list on error
    """
    try:
        supabase = get_supabase_client()
        response = supabase.table("packages").select("*").order("daily_rate").execute()
        
        if response.data:
            logger.info(f"Fetched {len(response.data)} packages from Supabase")
            return response.data
        else:
            logger.warning("No packages found in Supabase")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching packages from Supabase: {e}")
        return []


def get_dj_rate() -> float:
    """
    Fetch the DJ daily rate from the settings table.
    
    Returns:
        float: DJ daily rate in UGX, defaults to 550000 if not found
    """
    try:
        supabase = get_supabase_client()
        response = supabase.table("settings").select("dj_daily_rate").eq("id", 1).execute()
        
        if response.data and len(response.data) > 0:
            rate = float(response.data[0]['dj_daily_rate'])
            logger.info(f"Fetched DJ rate from Supabase: UGX {rate:,.0f}")
            return rate
        else:
            logger.warning("No DJ rate found in settings, using default: UGX 550,000")
            return 550000.0
            
    except Exception as e:
        logger.error(f"Error fetching DJ rate from Supabase: {e}")
        return 550000.0


def create_booking(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Create a new booking in Supabase (matches original schema).
    
    Args:
        data: Dictionary containing booking information:
            - customer_name: Customer's full name
            - email: Customer's email address
            - phone: Customer's phone number
            - start_date: Event start date (YYYY-MM-DD format)
            - end_date: Event end date (YYYY-MM-DD format)
            - package_id: ID of the selected package
            - qty: Quantity (number of packages)
            - include_dj: Boolean indicating if DJ service is included
            - total_price: Total booking price in UGX
            - status: Booking status (default: "pending")
    
    Returns:
        Dict: Created booking data with ID, or None on error
    """
    try:
        supabase = get_supabase_client()
        
        # Insert the booking
        response = supabase.table("bookings").insert(data).execute()
        
        if response.data:
            booking = response.data[0]
            logger.info(f"Created booking {booking.get('id')} for {data.get('customer_name')}")
            return booking
        else:
            logger.error("Failed to create booking: No data returned")
            return None
            
    except Exception as e:
        logger.error(f"Error creating booking in Supabase: {e}")
        return None


def list_bookings(status_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Fetch bookings from Supabase, optionally filtered by status.
    
    Args:
        status_filter: Optional status to filter by (e.g., "pending", "confirmed", "cancelled")
                      If None, returns all bookings
    
    Returns:
        List[Dict]: List of booking dictionaries, ordered by start_date descending
        
    Each booking contains:
        - id: Booking ID
        - customer_name: Customer's name
        - email: Customer's email
        - phone: Customer's phone
        - start_date: Event start date
        - end_date: Event end date
        - package_id: Package ID
        - qty: Quantity
        - include_dj: Boolean for DJ service
        - total_price: Total price in UGX
        - status: Booking status
    """
    try:
        supabase = get_supabase_client()
        
        # Build query
        query = supabase.table("bookings").select("*")
        
        # Apply status filter if provided
        if status_filter and status_filter != "all":
            query = query.eq("status", status_filter)
        
        # Order by start date (most recent first)
        response = query.order("start_date", desc=True).execute()
        
        if response.data:
            logger.info(f"Fetched {len(response.data)} bookings from Supabase")
            return response.data
        else:
            logger.info("No bookings found")
            return []
            
    except Exception as e:
        logger.error(f"Error fetching bookings from Supabase: {e}")
        return []


def update_booking_status(booking_id: int, new_status: str) -> Optional[Dict[str, Any]]:
    """
    Update the status of a booking in Supabase.
    
    Args:
        booking_id: ID of the booking to update
        new_status: New status value (e.g., "confirmed", "cancelled")
    
    Returns:
        Dict: Updated booking data, or None on error
    """
    try:
        supabase = get_supabase_client()
        
        # Update the booking status
        response = (
            supabase.table("bookings")
            .update({"status": new_status})
            .eq("id", booking_id)
            .execute()
        )
        
        if response.data:
            booking = response.data[0]
            logger.info(f"Updated booking {booking_id} status to {new_status}")
            return booking
        else:
            logger.error(f"Failed to update booking {booking_id}: No data returned")
            return None
            
    except Exception as e:
        logger.error(f"Error updating booking {booking_id} in Supabase: {e}")
        return None


def get_booking_by_id(booking_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a single booking by ID from Supabase.
    
    Args:
        booking_id: ID of the booking to fetch
    
    Returns:
        Dict: Booking data, or None if not found or on error
    """
    try:
        supabase = get_supabase_client()
        
        response = (
            supabase.table("bookings")
            .select("*")
            .eq("id", booking_id)
            .execute()
        )
        
        if response.data and len(response.data) > 0:
            logger.info(f"Fetched booking {booking_id} from Supabase")
            return response.data[0]
        else:
            logger.warning(f"Booking {booking_id} not found")
            return None
            
    except Exception as e:
        logger.error(f"Error fetching booking {booking_id} from Supabase: {e}")
        return None
