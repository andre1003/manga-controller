from django.urls import path

from manga_collections.views import *

urlpatterns = [
    path('my-collections/', my_collections, name='my_collections'),
    path('register/', collection_register, name='collection_register'),
    path('update/<uuid:id>/', collection_update, name='collection_update'),
    path('delete/<uuid:id>/', collection_delete, name='collection_delete'),
]
