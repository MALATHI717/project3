from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
     path('base/', views.base_view, name='base'),
    path('logout/', views.logout_view, name='logout')
]
