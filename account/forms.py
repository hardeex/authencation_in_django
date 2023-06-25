from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError




class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))
    # add more field as you desire and do not forget to add to the field in the class meta below to display it on the screen

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'password1', 'password2')  

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)   

        # styling the django fields
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
     
    # validating the registered email to ensure no email address is used multiple times  
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Err!: This email address is already in use.')
        return email

    # validating the registered email to ensure no email address is used multiple times 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=username).exists():
            raise forms.ValidationError('Err!: This username is already in use')
        return username


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100,  widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'new_password1', 'new_password2')  