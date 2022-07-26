from django import forms
from authorizations.models import User


class UserForm(forms.ModelForm):
	username = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	class Meta:
		model = User
		fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
	username = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
	last_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
	avatar = forms.ImageField(label='', required=False)
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'avatar']

