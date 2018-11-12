from django import forms
from .models import LoginUser

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, min_length=6,
                               label='账号', help_text='最小6位，最多20位')
    password = forms.CharField(max_length=12,min_length=6,widget=forms.PasswordInput(),
                               label='密码', help_text="最小6位，最长12位")

    portrait = forms.ImageField(label='头像', required=False)

    class Meta:
        model = LoginUser
        fields = ['username', 'password', 'portrait']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6,
                               label='账号', help_text='最小6位，最多20位')
    password = forms.CharField(max_length=12, min_length=6, widget=forms.PasswordInput(),
                               label='密码', help_text="最小6位，最长12位")
