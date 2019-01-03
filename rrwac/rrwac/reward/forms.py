from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.validators import RegexValidator

import re


def lowercase_email(email):
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = '@'.join([email_name.lower(), domain_part.lower()])
    return email


class SignupForm (forms.ModelForm):

    username = forms.CharField(
        label='Student Name',
        required=True,
        error_messages={'required': 'Please Input Your Full Name', 'max_length': 'Max Input is 30 Digits', 'min_length': 'Min Input is 3 Digits'},
        max_length=30,
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': '3~30 Characters'})
    )
    email = forms.EmailField(
        error_messages={'required': 'Please Input Your Email', 'invalid': 'Email Format is not Right'},
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    id = forms.CharField(
        label='Student Number',
        required=True,
        error_messages={'required': 'Your Student Number', 'max_length': 'Student Number is a 7 Digits Number', 'min_length': 'Student Number is a 7 Digits Number符'},
        max_length=7,
        min_length=7,
        validators=[RegexValidator(r'^\d{1,10}$')], widget=forms.TextInput(attrs={'placeholder': '7 Digits Number'})
    )
    password = forms.CharField(
        error_messages={'required': 'Please Input Password', 'max_length': 'Max Input is 20 Digits', 'min_length': 'Min Input is 6 Digits'},
        label='Password',
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '6 to 60 Digits Password'})
    )
    confirm_password = forms.CharField(
        error_messages={'required': 'Please Input Password', 'max_length': 'Max Input is 20 Digits', 'min_length': 'Min Input is 6 Digits'},
        label='Confirm Password',
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password'})
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "id")

    def clean_email(self):
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        lower_email = lowercase_email(email)
        try:
            UserModel._default_manager.get(email=lower_email)
        except UserModel.DoesNotExist:
            return lower_email
        raise forms.ValidationError("Somebody had registered with this Email")

    def clean_id(self):
        UserModel = get_user_model()
        id = self.cleaned_data["id"]
        student_number = id
        try:
            UserModel._default_manager.get(id=student_number)
        except UserModel.DoesNotExist:
            return student_number
        raise forms.ValidationError("Somebody had registered with this Student Number")

    def clean_confirm_password(self):
        # cleaned_data=super(SignupForm,self).clean()
        password = self.cleaned_data.get("password", False)
        confirm_password = self.cleaned_data["confirm_password"]
        if not(password == confirm_password):
            raise forms.ValidationError("Password and Confirm Password are not SAME")
        return confirm_password


class LoginForm (forms.Form):

    username = forms.CharField(
        label='username', required=False)
    password = forms.CharField(
        label='Password', required=False, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        UserModel = get_user_model()
        username = cleaned_data.get("username")
        username = username.strip()
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                return cleaned_data
            else:
                raise forms.ValidationError("This Account is not Actived")

        else:
            raise forms.ValidationError("This Account is not registered")

        if not username or not password:
            raise forms.ValidationError("username/Password cannot be empty")

        else:
            raise forms.ValidationError("username and Password does not Match")


class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        error_messages={'required': 'Old Password incorrect', 'max_length': 'Max Input is 20 Digits', 'min_length': 'Min Input is 6 Digits'},
        label='Password',
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '6 to 60 Digits Password'})
    )
    newpassword1 = forms.CharField(
        error_messages={'required': 'Please Input Password', 'max_length': 'Max Input is 20 Digits', 'min_length': 'Min Input is 6 Digits'},
        label='Password',
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '6 to 60 Digits Password'})
    )
    newpassword2 = forms.CharField(
        error_messages={'required': 'New Password does not Match', 'max_length': 'Max Input is 20 Digits', 'min_length': 'Min Input is 6 Digits'},
        label='Password',
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '6 to 60 Digits Password'})
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('You have to fill all blanks')
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data

    def clean_newpassword2(self):
        newpassword1 = self.cleaned_data.get("newpassword1", False)
        newpassword2 = self.cleaned_data["newpassword2"]
        if not(newpassword1 == newpassword2):
            raise forms.ValidationError("New Password and Confirm Password are not SAME")
        return newpassword2
