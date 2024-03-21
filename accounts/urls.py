from django.urls import path    
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('base/', views.base_view, name='base'),
    path('home/', views.home_view, name='home'),
]