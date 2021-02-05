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
    name = models.CharField(max_length=11, null=False, blank=False)
    # class Meta:
    #     verbose_name = 'Doctor'
    def __str__(self):
        return self.user.username

