from datetime import time
from .models import Order

def check_available_slots(date):
    all_slots  = [time(9,0),time(10,0),time(11,0),time(12,0),time(13,0),time(14,0),time(15,0),time(16,0),time(17,0),]

    booked_slots = set(Order.objects.filter(date=date).values_list('time',flat=True))
    
    available = [slot for slot in all_slots if slot not in booked_slots]
    return available
    
    # for slot in all_slots:
    #     if slot not in booked_slots:
    #         available.append(slot)

