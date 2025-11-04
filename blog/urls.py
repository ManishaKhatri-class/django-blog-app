
from django.contrib import admin
from django.urls import path
from blog import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),#show post by primary key int
     path('post/new/', PostCreateView.as_view(),name='post-create'),#to create new post
      path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),#to update new post
       path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),#to delete post
    path('about/',views.about,name='blog-about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#create post_list.html in templates in views.py 