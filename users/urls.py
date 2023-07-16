from django.urls import path

from .views import *


urlpatterns = [
    path('register/', user_register, name='user_register'),
    path('edit/', user_update, name='user_update'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
