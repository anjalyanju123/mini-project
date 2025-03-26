from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('authregister/',authregister,name='authregister'),
    path('Profile/',Profile,name='Profile'),
    path('authlogin/',authlogin,name='authlogin'),
    path('authlogout/',authlogout,name='authlogout'),
    path('book_list/',book_list,name='book_list'),
    path('reset_password/<int:user_id>/',reset_password, name='reset_password'),
    path('Edit_profile/',Edit_profile, name='Edit_profile'),
]