from django.urls import path
from authapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]