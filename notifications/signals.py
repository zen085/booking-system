import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from bookings.models import Order


logger = logging.getLogger(__name__)

@receiver(post_save,sender=Order)
def create_order_signals(sender,instance,created,**kwargs):
    if created:
        logger.info(f"Book created:{instance.id}")
        




