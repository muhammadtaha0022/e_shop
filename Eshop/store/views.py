# from django.shortcuts import render
# from django.http import HttpResponse
# from .models.product import Product
# from .models.category import category



# # Create your views here.
# def index(request):
#     product = Product.get_all_products()
#     category = category.get_all_category()
#     data={}
#     data['product']= product
#     data['category']= category
#     return render(request, 'index.html', data)

from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import category  # Use PascalCase for class names
from .models.customer import Customer

# Create your views here.
def index(request):
    products = None  # Use snake_case for variables
    categories = category.get_all_categories()  # Use snake_case for variables
    categoryid = request.GET.get('category')
    if categoryid:
        products= Product.get_all_products_by_categoryid(categoryid)
    else:
        products = Product.get_all_products()
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', data)



def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postdata = request.POST
        first_name=postdata.get('firstname')
        last_name=postdata.get('lastname')
        phone=postdata.get('phone')
        password=postdata.get('password')
        email=postdata.get('email')
        print(first_name,last_name,phone,email,password)
        customer =Customer( first_name=first_name,
                        last_name= last_name,
                        phone= phone,
                        email=email,
                        password= password)
           
        customer.register()
        return HttpResponse('success')