

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
import logging

from bookings.models import Order
from notifications.models import Notifications


logger = logging.getLogger(__name__)


@shared_task
def create_notification(order_id):

    try:
        order = Order.objects.select_related("user").get(id=order_id)

    except Order.DoesNotExist:
        logger.error(f"Order with id {order_id} does not exist")
        return

    #  Email comes from booking form
    recipient_email = order.email

    if not recipient_email:
        logger.error(f"Order {order.id} has no email")
        return

    subject = f"Booking #{order.id} Pending"

    message = (
        f"Hello {order.name},\n\n"
        f"Your booking for {order.service} has been successfully placed."
    )

    logger.info(f"Sending email to {recipient_email} for order {order.id}")

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False
        )

        status = "SENT"

        logger.info(f"Book Email successfully sent to {recipient_email}")

    except Exception as e:

        status = "FAILED"

        logger.error(
            f"Email sending failed for {recipient_email} "
            f"(order {order.id}): {e}"
        )

    # Always create notification record (success or failure)
    try:
        with transaction.atomic():
            Notifications.objects.create(
                order=order,
                notifications_type="EMAIL",
                recipient=order.user,
                recipient_email=recipient_email,
                message=message,
                status=status
            )

    except Exception as db_error:
        logger.error(
            f"Failed to save notification for order {order.id}: {db_error}"
        )


@shared_task
def confirmation_notification(order_id):

    try:
        order = Order.objects.select_related("user").get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f"Order {order_id} not found")
        return

    recipient_email = order.email

    if not recipient_email:
        logger.error(f"Order {order.id} has no email")
        return

    subject = f"Booking #{order.id} Confirmation"

    message = (
        f"Hello {order.name},\n\n"
        f"Your booking for {order.service} "
        f"has been confirmed successfully."
    )

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False
        )
        status = "SENT"
        logger.info(f"Confirmation Email successfully sent to {recipient_email} for book {order.id} ")

    except Exception as e:
        logger.error(f"Confirmation email failed: {e}")
        status = "FAILED"

    # save notification record 
    Notifications.objects.create(
        order=order,
        notifications_type="EMAIL",
        recipient=order.user,
        recipient_email=recipient_email,
        message=message,
        status=status
    )




@shared_task
def cancellation_notification(order_id):

    try:
        order = Order.objects.select_related("user").get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f"Order {order_id} not found")
        return

    recipient_email = order.email

    if not recipient_email:
        logger.error(f"Order {order.id} has no email")
        return

    subject = f"Booking #{order.id} Cancelled"

    message = (
        f"Hello {order.name},\n\n"
        f"Your booking for {order.service} "
        f"has been cancelled successfully."
    )

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False
        )
        status = "SENT"
        logger.info(f" Cancellation Email successfully sent to {recipient_email} for book {order.id} ")

    except Exception as e:
        logger.error(f"Cancellation email failed: {e}")
        status = "FAILED"

    # save notification record 
    Notifications.objects.create(
        order=order,
        notifications_type="EMAIL",
        recipient=order.user,
        recipient_email=recipient_email,
        message=message,
        status=status
    )