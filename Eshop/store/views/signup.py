from django.shortcuts import render ,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View





# signup design for e shop 
class signup(View):
    def get(self, request):
         return render(request,'signup.html')
    
    def post(self, request):
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
        error_message = self.validateCustomer(customer)


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


    def validateCustomer(self,customer):
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
            error_message= " phone  is required "
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


    # def registerUser(request):