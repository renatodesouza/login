from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class PageView(TemplateView):
    template_name = 'login/page1.html'

class MyLoginView(TemplateView):
    template_name = 'registration/login.html'

class HomeView(TemplateView):
    template_name = 'login/home.html'

class UserView(TemplateView):
    template_name = 'login/user.html'

def my_login(request):
    username = request.GET['username']
    password = request.GET['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect('user')
    else:
        message_error = 'Usuario não encontrado'
        return render(request, 'login/home.html', {context:message_error})

