from django.db import models
from django.contrib.auth.models import User
from home_page.models import Service

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=20,)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING') 
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField()   


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'time'], name='unique_booking_slot')
        ]
    
    def __str__(self):
        return f"Booked {self.service} by {self.user_id}, time {self.time}, date {self.date}"