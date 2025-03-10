from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField(max_length=50, default="",blank=True)
    address = models.CharField(max_length=500,default="",blank=True)
    phone = models.CharField(max_length=50,default="",blank=True)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    
    def placeorder(self):
        self.save()
        
        
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')
    
