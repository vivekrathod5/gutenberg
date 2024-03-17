from django.urls import path
from .views import book_list_api

urlpatterns = [
    path('list/', book_list_api, name='book-list'),
]
