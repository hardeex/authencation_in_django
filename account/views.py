from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm, PasswordChangedForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin




# Create your views here.
class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')




class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangedForm    
    success_url = reverse_lazy('account:changed_password_successfully') 

def changed_password_successfully(request):
    return render(request, 'users/changed_password_successfully.html')




class ForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/forgot_password.html'
    email_template_name = 'users/forgot_password_email.html'
    subject_template_name = 'registration/forgot_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')