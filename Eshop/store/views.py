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

from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import category  # Use PascalCase for class names
from .models.customer import Customer
from django.contrib.auth.hashers import make_password ,check_password
from django.views import View

print(make_password('1234'))
print(check_password('1234','pbkdf2_sha256$870000$MgSW0l5mSw9nq6eOJllaSd$4O9jt0ptMbI1xMkqDsrIgqqrPDCYTi/3X72j5m5q0M4='))



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





def validateCustomer(customer):
        error_message = None;
        if(not customer.first_name):
            error_message= "First name is required !!"
        elif len(customer.first_name) < 4 :
             error_message= "First name is more then 4 character "
        elif (not customer.last_name):
            error_message= "last name required"
        elif len(customer.last_name) < 4:
            error_message = " last name must be 4 character long or more "
        elif (not customer.phone):
            error_message= " error message is required "
        elif len(customer.phone)< 11:
            error_message = "enter full number"
        elif (not customer.email):
            error_message="enter a valid email"
        elif len(customer.email)<5:
            error_message="email must be 6 character"
        elif (not customer.password):
            error_message= "enter a password"
        elif len(customer.password)<4:
            error_message="password must be 4 character or more"
        elif customer.isexist():
            error_message = 'email address already register '    
        
        return error_message


def registerUser(request):
        postdata = request.POST
        first_name=postdata.get('firstname')
        last_name=postdata.get('lastname')
        phone=postdata.get('phone')
        password=postdata.get('password')
        email=postdata.get('email')
        # validation start
        value={
            'first_name ': first_name,
            'last_name ': last_name,
            'phone':phone,
            'email': email,
        }
        error_message = None

        customer =Customer( first_name=first_name,
                            last_name= last_name,
                            phone= phone,
                            email=email,
                            password= password)
        error_message = validateCustomer(customer)


        #  validation end
        if not error_message: 
                
            print(first_name,last_name,phone,email,password)
            
            customer.password = make_password(customer.password )    
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'value':value
            }
            return render(request,'signup.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        return registerUser(request)

        

class login(View):
    def get(self, request ):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'email or password invalid !!'
        else:
            error_message = 'email or password invalid !!'
        print(email,password)
        return render(request, 'login.html',{'error': error_message})


