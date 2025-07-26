from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.index, name='book_list'),
    path('example-form/', views.example_view, name='example_form'),
]
