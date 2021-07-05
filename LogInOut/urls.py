from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'LogInOut'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',views.LogoutView.as_view(next_page='/LogInOut/login/'),name='logout'),
]