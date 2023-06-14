from django.urls import path
from authapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('request-reset-email/', views.RequestReserEmailView.as_view(), name="request-reset-email"),
    path('set-new-password/<uidb64>/<token>', views.SetNewPasswordView.as_view(), name='set-new-password'),
]