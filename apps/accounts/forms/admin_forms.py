from django import forms
from apps.accounts.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from apps.accounts.models import Profile

        
class SingUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','groups','password1','password2']
        
        
class ChangeAdminForm(UserChangeForm):
    class Meta:
        model = User
        # fields = ['username','email','first_name','last_name','groups','phone_number','country','city','address','image','is_active','is_staff']
        exclude = ['password','user_permissions','date_joined','last_login','is_superuser']
# class ProfileAdminForm(forms.ModelForm):
    
#     class Meta:
#         model = Profile
#         exclude = ['user']
        