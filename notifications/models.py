from django.db import models
from django.contrib.auth.models import User
from bookings.models import Order


class Notifications(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),        
        ('FAILED', 'Failed'),
        ]
    
    TYPE_EMAIL = "EMAIL"
    TYPE_SMS = "SMS"

    TYPE_CHOICES = [
        (TYPE_EMAIL, "Email"),
        (TYPE_SMS, "SMS"),
    ]


    notifications_type = models.CharField(choices=TYPE_CHOICES,max_length=25)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="notifications")

    def __str__(self):
        return f"{self.notifications_type} to {self.recipient} ({self.status})"
    
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        indexes = [
        models.Index(fields=['status']),
        models.Index(fields=['created_at']),
    ]
        
        constraints = [
            models.UniqueConstraint(
                fields=["order", "notifications_type"],
                name="unique_notification_per_order_type"
            )
        ]
        
   
    

