from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    index,
    profile,
    PostList,
    postcreate,
    PostDetailView,
    dropzone_image
    )
    
app_name="posts"

urlpatterns = [

    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('postlist/', PostList.as_view(), name='postlist'),
    path('postcreate/', postcreate, name='postcreate'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='postdetail'),
    path('dropzone-image', dropzone_image, name='dropzone-image'),

    ]