from django.urls import path, include
from django.contrib.auth import views as authViews
from django.contrib import admin
from .views import register, index, logout, loginsee, user_list, Blog_view,blog_create

urlpatterns = [
    path('', index, name = 'index'),
    path('register', register, name='register'),
    path('login', loginsee, name='login'),
    path('accounts/logout/', authViews.LogoutView.as_view(next_page = 'index'), name='logout'),
    path('user_list', user_list, name='user_list'),
    path('blog', Blog_view, name='blog'),
    path('blog_create',blog_create, name= 'blog_create')
]