from django.db import models

# Create your models here.

class Orders(models.Model):   
    product_name = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(max_length=250, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f'{self.product_name}'