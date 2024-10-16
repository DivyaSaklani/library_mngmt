# library/urls.py
from django.urls import path
""" from .views import book_list, add_book """
from .views import login_view, book_list, add_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('login/', login_view, name='login'),
]