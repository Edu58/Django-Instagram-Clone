from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
]
