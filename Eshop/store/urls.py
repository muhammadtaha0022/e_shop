from django.urls import path
from .views import home , login , signup
from .views.home import index  
from store.views.login import logout
from .views.cart import cart
from  . import views 
from .views.checkout import Checkout 
from . import views
from .views.orders import orderview


urlpatterns = [
    path('', index.as_view() , name = 'homepage'),
    path('login/' , login.login.as_view() , name='login'),
    path('signup/' , signup.signup.as_view() , name='signup'),
    path('logout/' , logout , name='logout'),
    path('cart/' , cart.as_view()  , name='cart'),
    path('check_out/' , Checkout.as_view()  , name='checkout'),
    path('orders/' , orderview.as_view()  , name='orders'),


]
