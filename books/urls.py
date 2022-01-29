from django.urls import path
from .views import *
urlpatterns = [
    path('books/',booksapi.as_view()),
    path('users/',userapi.as_view()),
    path('order/',orderbook.as_view()),

]
