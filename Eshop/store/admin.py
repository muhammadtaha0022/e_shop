from django.contrib import admin
from .models.product import Product
from .models.category import category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.

class adminproduct(admin.ModelAdmin):
    list_display=['name', 'price', 'category']


class admincategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product, adminproduct)
admin.site.register(category,admincategory)
admin.site.register(Customer)
admin.site.register(Order)

