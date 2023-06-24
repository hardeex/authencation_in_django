from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
#from index.models import Profile
#from django.forms import ImageField
from django.core.exceptions import ValidationError
#from index.models import Comment
#from ckeditor.widgets import CKEditorWidget
#from mptt.forms import TreeNodeChoiceField
#from contact.models import Contact



class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email',  'password1', 'password2')  

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)   

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
     
          
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('ERROR: This email address is already in use.')
        return email
