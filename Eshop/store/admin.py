from django.contrib import admin
from .models.product import Product
from .models.category import category
from .models.customer import Customer

# Register your models here.

class adminproduct(admin.ModelAdmin):
    list_display=['name', 'price', 'category']


class admincategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product, adminproduct)
admin.site.register(category,admincategory)
admin.site.register(Customer)
