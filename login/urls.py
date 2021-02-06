from django.urls import path
from . import views

from .views import PageView, MyLoginView, HomeView, UserView

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


app_name = 'login'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/', UserView.as_view(), name='user'),
    path('page1/', PageView.as_view(), name='page1'),
    #path('login/', MyLoginView.as_view(), name='login'),
    
    

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/index.html'), name='logout'),
]