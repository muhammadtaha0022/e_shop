from django.urls import path
from .views import index , signup , login
from  . import views 
urlpatterns = [
    path('',index, name = 'homepage'),
    path('signup/', views.signup, name = 'signup'),
    # path('login/', views.login, name = 'login')
    path('login/' , login.as_view())
]
