from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, PostDetailView, PostCreateView, PostUpdateView, 
    PostDeleteView, register, profile, add_comment, edit_comment, delete_comment,
    posts_by_tag
)

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('tag/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:home'), name='logout'),
    path('profile/', profile, name='profile'),
]