from django.urls import path
from . import views
from . views import UserRegisterView, ChangePasswordView, ForgotPasswordView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # the login will work fine without this path, I use so you can style the page to your taste

    path('login_success/', views.login_success, name='login_success'),

    path('change_password/', ChangePasswordView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('changed_password_successfully/', views.changed_password_successfully, name='changed_password_successfully'),

    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'), 
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]