from django.contrib.auth.models import User
from django import forms

error_messages_pl = {
    'required' : 'To pole jest wymagane',
    'invalid' : 'Wprowadź poprawną wartość'
}

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Username', error_messages=error_messages_pl)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Email', error_messages=error_messages_pl)
    password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password', error_messages=error_messages_pl)
    confirm_password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirm password', error_messages=error_messages_pl)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')


class CustomerLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Email', error_messages=error_messages_pl)
    password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password', error_messages=error_messages_pl)

    class Meta:
        model = User
        fields = ('email', 'password')