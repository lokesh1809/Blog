from django import forms
from main import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ('title', 'content')

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 256)
    password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.CharField(widget = forms.EmailInput())
    username = forms.CharField(max_length = 256)
    first_name = forms.CharField(max_length = 256)
    last_name = forms.CharField(max_length = 256)
    password = forms.CharField(widget = forms.PasswordInput)

    