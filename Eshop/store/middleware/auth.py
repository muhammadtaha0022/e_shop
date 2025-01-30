from django.shortcuts import render, redirect

def auth_middleware(get_response):


    def middleware(request):
        if not request.session.get('customer'):
            return redirect('login')

        response = get_response(request)


        return response

    return middleware