from django import forms
from .models import *
from django.core.validators import *


class Student_from(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'Class': 'form control','placeholder': 'Enter your name'}),required=True,max_length=50)
    #name= forms.CharField((widget=forms.TextInput(attrs={'Class': 'form control','placeholder': 'Enter your name'})required=True,max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'Class': 'form control','placeholder': 'Enter your ,email'}),max_length=50)
    phone = forms.CharField(widget=forms.TextInput(attrs={'Class': 'form control','placeholder': 'Enter your phone number'}),required=True, max_length=11)
    dob= forms.DateTimeField(widget=forms.TextInput(attrs={'Class': 'form control','placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Student
        fields = ['name','email','phone','dob']

        def clean_email(self):
            email_id = self.cleaned_email['email']
            try:
                match = Student.objects.get(email = email_id)
            except:
                return self.cleaned_data['email']
            raise forms.ValidationError('email already exist')