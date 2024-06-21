from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Student, Counsellor

class CustomStudentPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class CustomCounsellorPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name', 'email']

class CounsellorProfileForm(forms.ModelForm):
    class Meta:
        model = Counsellor
        fields = ['first_name','last_name', 'staff_id', 'email','gender','year_of_experience', 'religion']