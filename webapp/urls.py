from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views

app_name = 'webapp'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='webapp/logout.html'), name='logout'),
    path('change-password/', views.change_password, name='change-password'),
    # Reset password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='webapp/password_reset.html', success_url='password_reset_done'),
         name='password_reset'),
    path('password-reset/password_reset_done',
         auth_views.PasswordResetDoneView.as_view(template_name='webapp/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='webapp/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='webapp/password_reset_complete.html'),
         name='password_reset_complete'),
]