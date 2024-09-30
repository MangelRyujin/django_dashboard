from django import forms
from apps.accounts.models import User
from django.contrib.auth.forms import UserCreationForm

# from apps.accounts.models import Profile

        
class RegisterForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']