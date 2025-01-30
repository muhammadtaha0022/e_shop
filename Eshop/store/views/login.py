from django.shortcuts import render ,redirect


from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View








# login design for e shop 
class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer'] = customer.id
                    
                return redirect('homepage')
            else:
                error_message = 'email or password invalid !!'
        else:
            error_message = 'email or password invalid !!'
        print(email,password)
        return render(request, 'login.html',{'error': error_message})   
    
    
    



def logout(request):
    request.session.clear()
    return redirect('login')