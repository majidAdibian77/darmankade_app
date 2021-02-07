from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.


# class Patient(AbstractUser):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userProfileInfo")
#     phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
#
#     def __str__(self):
#         return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient")
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    # REQUIRED_FIELDS = ['username', 'password1', 'password2', phone_number]
    # USERNAME_FIELD = 'username'
    # class Meta:
    #     verbose_name = 'Patient'
    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    name = models.CharField(max_length=50, null=False, blank=False)
    speciality = models.CharField(max_length=50, null=False, blank=False)
    doctor_number = models.IntegerField( null=False, blank=False)
    online_payment = models.BooleanField(default=False)
    experience_year = models.SmallIntegerField(null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    week_days = models.CharField(max_length=150, null=False, blank=False)
    photo = models.ImageField(null=False, blank=False, upload_to='doctor_profile')

    def __str__(self):
        return self.user.username


class Star(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='stars')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='stars')
    score = models.SmallIntegerField(null=False, blank=False, default=0)


class Comment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='commets')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='commets')
    text = models.TextField(max_length=500 ,null=False, blank=False)