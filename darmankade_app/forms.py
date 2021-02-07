from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from darmankade_app.models import Patient, Doctor


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('phone_number',)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'speciality', 'doctor_number', 'online_payment', 'experience_year',
                  'address', 'phone_number', 'photo')

