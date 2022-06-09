from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('upload/', views.upload, name='upload'),
    path('comment/<int:image_id>', views.comment, name='comment'),
    path('search/', views.search, name='search'),
    path('like/<post_id>',views.like_post, name='like'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
