from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    
    # Document management URLs with permission checks
    path('documents/', views.document_list_view, name='document_list'),
    path('documents/<int:pk>/', views.document_detail_view, name='document_detail'),
    path('documents/create/', views.document_create_view, name='document_create'),
    path('documents/<int:pk>/edit/', views.document_edit_view, name='document_edit'),
    path('documents/<int:pk>/delete/', views.document_delete_view, name='document_delete'),
    
    # Permission denied page
    path('permission-denied/', views.permission_denied_view, name='permission_denied'),
]
