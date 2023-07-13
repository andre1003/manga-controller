from django.urls import path

from mangas.views import *


urlpatterns = [
    path('register/', manga_register, name='manga_register'),
    path('my-mangas/', my_mangas, name='my_mangas'),
    path('update/<uuid:id>', manga_update, name='manga_update'),
    path('delete/<uuid:id>', manga_delete, name='manga_delete'),
]
