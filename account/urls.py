from django.urls import path
from . import views
from . views import UserRegisterView


app_name: 'account'

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),
]