from django.core.exceptions import ValidationError
from .models import Order
from datetime import date
import re

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?[0-9\s\-]{7,15}$'



def date_logic(booking_date):
   
    if not booking_date:
        raise ValidationError("Date is required.")

    if booking_date < date.today():
        raise ValidationError("You can not book a past date.")
    return booking_date
   
def  name_logic(name):

    if not name:
        raise ValidationError("Name is required.")

    if len(name) < 3:
        raise ValidationError("Name is too short.")
    return name

def email_logic(email):

    if not email:
        raise ValidationError("Email address is required.")

    if not re.match(EMAIL_REGEX,email):
        raise ValidationError("Enter valid email address.")
    return email

def phone_logic(phone):
    
    if not phone:
        raise ValidationError("Phone number is required.")

    if not re.match(PHONE_REGEX,phone):
        raise ValidationError("Enter valid phone number.")
    return phone


def check_fields(service,time,notes):
    
    if not service or not time or not notes:
        raise ValidationError("Fill all required fields.")
    

def slot_check(date,time):
    
    if date and time:
        if Order.objects.filter(date=date,time=time).exists():
            raise ValidationError("This time slot is arleady booked.")
        


# def slot_in_use(date,time):
#     return Order.objects.filter(date=date,time=time).exists()