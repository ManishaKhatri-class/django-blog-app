
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/',views.about,name='blog-about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


