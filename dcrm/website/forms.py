from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class SingUpUserForm(UserCreationForm):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SingUpUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})




class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='')
    last_name = forms.CharField(max_length=50, label='')
    email = forms.EmailField(max_length=100, label='')
    phone = forms.CharField(max_length=15, label='')
    address = forms.CharField(max_length=100, label='')

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
