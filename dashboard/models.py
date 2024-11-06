from django.db import models

# Create your models here.

class Dashboard(models.Model):  
    total_earnings = models.IntegerField(default=0)
    total_orders = models.IntegerField(default=0)
    total_deliveries= models.IntegerField(default=0)
    canceled_orders = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.total_earnings}'