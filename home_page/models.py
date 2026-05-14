from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return f'{self.name}'