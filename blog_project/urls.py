from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('author/', include('author.urls')),
    path('category/', include('categories.urls')),
    path('post/', include('post.urls')),
    path('profiles/', include('profiles.urls')),
]
