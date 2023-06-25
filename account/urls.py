from django.urls import path
from . import views
from . views import UserRegisterView, ChangePasswordView, ForgotPasswordView
from django.contrib.auth import views as auth_views

app_name: 'account'

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),

    path('password/', ChangePasswordView.as_view(template_name='users/change_password.html'), name='password'),
    path('changed_password_successfully/', views.changed_password_successfully, name='changed_password_successfully'),

    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'), 
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]