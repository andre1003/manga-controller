from django.urls import path

from anime.views import *


urlpatterns = [
    path('my-animes/', my_animes, name='my_animes'),
    path('register/', anime_register, name='anime_register'),
    path('update/<uuid:id>', anime_update, name='anime_update'),
    path('delete/<uuid:id>', anime_delete, name='anime_delete'),
]
