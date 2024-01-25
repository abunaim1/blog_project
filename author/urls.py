from django.urls import path
from . import views
urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),
   path('profile/', views.profile, name='profile'),
   path('profile/edit', views.update_profile, name='update_profile'),
   path('profile/password/', views.password_change, name='password_change'),
]
