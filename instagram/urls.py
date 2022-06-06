from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('comment/<int:image_id>', views.comment, name='comment'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
]
