from django.db import models

# Create your models here.
class Customers(models.Model): 
    full_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}'