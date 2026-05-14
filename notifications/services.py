from bookings.models import Order
from notifications.tasks import create_notification,confirmation_notification,cancellation_notification


def create_order(user,name,email,phone,service,date,time,notes):
    order = Order.objects.create(
        user=user,
        name=name,
        email=email,
        phone=phone,
        service=service,
        date=date,
        time=time,
        notes=notes,
        )
    
    create_notification.delay(order.id)
    return order

def confirmed_order(order):
    confirmation_notification.delay(order.id)
    


def cancel_order(order):
    if order.status == "CANCELLED":
        return
        
    order.status = "CANCELLED"
    order.save()
    cancellation_notification.delay(order.id)

      
           
