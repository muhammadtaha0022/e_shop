from django.db import models
from .category import category

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True,null=True )
    image=models.ImageField(upload_to='uploads/products/', height_field=None, width_field=None, max_length=None)
    


    @staticmethod
    def get_all_products():
        return Product.objects.all()
    

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id )
        else:
            return Product.get_all_products()
            return Product.objects.all()