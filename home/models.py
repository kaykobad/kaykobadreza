from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email_address = models.EmailField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.email_address