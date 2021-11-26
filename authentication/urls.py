from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView

urlpatterns = [
     # Auth views
     path('api/user/auth/login/',LoginView.as_view(), name='auth_login'),

     path('api/user/auth/logout/',LogoutView.as_view(), name='auth_logout'),

     path('api/user/auth/signup/',SignupView.as_view(), name='auth_signup'),

     path('api/user/auth/reset/',include('django_rest_passwordreset.urls',namespace='password_reset')),

     path('api/user/profile/',ProfileView.as_view(), name='user_profile'),
]