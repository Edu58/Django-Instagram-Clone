from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('comment/<int:image_id>', views.comment, name='comment'),
    path('search/', views.search, name='search'),
    path('like/<user_id>/<post_id>',views.like_image, name='like'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
