from django import forms
from django.contrib.auth.models import User
from.models import Customer,Task



class  CustomerUserForm(forms.ModelForm):        
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'image']
        widgets = {
            'mobile': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': 'Enter mobile number',
                'class': 'mobile-input'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter address'
            }),
        }

        
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task_name','date']
        widgets = {
            'task_name': forms.TextInput(attrs={'placeholder': 'Enter task name'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }