from typing import Any, Dict
from django import forms
from django.core import validators
# widgets == field to html input

"""class contactForm(forms.Form):
    name=forms.CharField(label="Full Name :",help_text="Total length must be within 70 character",
        required=False,disabled=False,widget=forms.Textarea(attrs ={'id': 'textarea','class':'class 1 class 2',
        'placeholder':"Enter your name "})) #for by default , false sign for remove * sign, disabled- kichu change kora jabe na
    email=forms.EmailField(label="User Email")
    # age= forms.IntegerField()
    # weight= forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal=[('P','Pepperoni'),('M','Mushroom'),('B','Beef')]
    pizza=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    file=forms.FileField(required=False)"""

"""class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<10:
            raise forms.ValidationError("Enter a name with at least at least 10 character")
        return valname
    
    def clean_email(self):
        valemail=self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("Your email must contain .com")
        return valemail
        
    def clean(self):
        clean_field =super().clean()
        valname= self.cleaned_data['name']
        valemail= self.cleaned_data['email']
        if len(valname)<10:
            raise forms.ValidationError("Enter a name with at least at least 10 character")
        if '.com' not in valemail:
            raise forms.ValidationError("Your email must contain .com")"""
            
def len_check(value):
    if(len(value))<10:
        raise forms.ValidationError("Enter a value at least 10 chars")
    
class StudentData(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(10,
                        message="Enter a name with at least at least 10 characters")])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email")])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message="Age should be maximum 34"
                        ),validators.MinValueValidator(24,message="Age should be at least 24")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],
                        message="file extension must be ended with .pdf")])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])   


class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput) 
    
    def clean(self):
        clean_field=super().clean()
        valpass=self.cleaned_data['password']
        valconpass=self.cleaned_data['confirm_password']
        valname=self.cleaned_data['name']
        if valpass!=valconpass:
            raise forms.ValidationError("Password doesn't match")
        if len(valname)>15:
            raise forms.ValidationError("name must be in 15 chars")
    