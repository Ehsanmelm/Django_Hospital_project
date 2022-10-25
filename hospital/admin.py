from django.contrib import admin
from .models import DoctorModel, PatientModel

# Register your models here.


class DockAmin(admin.ModelAdmin):
    list_display = ["Doct_name", "status"]


class patientAmin(admin.ModelAdmin):
    list_display = ["Patient_name", "is_accepted"]


admin.site.register(DoctorModel, DockAmin)
admin.site.register(PatientModel, patientAmin)
