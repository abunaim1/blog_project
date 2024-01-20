
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('category/', include('categories.urls')),
    path('post/', include('post.urls')),
    path('profiles/', include('profiles.urls')),
]
