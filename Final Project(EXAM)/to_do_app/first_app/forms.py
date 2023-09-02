from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import UserAccount
from django.contrib.auth.models import User

class loginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    university=forms.CharField(max_length=70)
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name','university']
        
    def save(self,commit=True):
        our_user=super().save(commit=False)
        if commit==True:
            our_user.save()
            
            
class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'email']
    def save(self,commit=True):
        our_user=super().save(commit=False)
        if commit==True:
            our_user.save()


