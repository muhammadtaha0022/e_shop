from django.shortcuts import render ,redirect
from store.models.product import Product
from store.models.category import category  # Use PascalCase for class names
from django.views import View





class index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove') 
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity :
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                    
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
             cart = {}
             cart[product] = 1
             
        request.session['cart'] = cart
        print(cart ,request.session['cart'])
        return redirect('homepage')
    
    
    
    def get(self , request ):
        cart = request.session.get('cart')
        if not cart:
            request.session["cart"]= {}
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
        print('you are :' ,request.session.get('email'))
        return render(request, 'index.html', data)