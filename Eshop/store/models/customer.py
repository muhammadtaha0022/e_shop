from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,default='Unknown',null=True, blank=True)
    last_name = models.CharField(max_length=50 ,null=True, blank=True)
    phone = models.CharField( max_length=15)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=500)



    def register(self):
        self.save()
