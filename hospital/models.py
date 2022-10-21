from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class DoctorModel(models.Model):
    departments = [('Cardiologist', 'Cardiologist'),
                   ('Dermatologists', 'Dermatologists'),
                   ('Emergency Medicine Specialists',
                    'Emergency Medicine Specialists'),
                   ('Allergists/Immunologists', 'Allergists/Immunologists'),
                   ('Anesthesiologists', 'Anesthesiologists'),
                   ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
                   ]
    Doct_name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    profile_pic = models.ImageField(
        upload_to='upload/Doctor_Profile', null=True, blank=True)
    address = models.CharField(max_length=40)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)


class PatientModel(models.Model):
    Patient_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(
        upload_to='upload/Patinet_Profile', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.DateField(null=True)
    status = models.BooleanField(default=False)
