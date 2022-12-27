from django.contrib import admin
from .models import DoctorModel, PatientModel, AppointmentModel, DischargePatientModel

# Register your models here.


class DockAmin(admin.ModelAdmin):
    list_display = ["Doct_name", "status"]


class patientAmin(admin.ModelAdmin):
    list_display = ["patient_name", "is_accepted"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name']


class DischargedAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'assigned_doctor_name']


admin.site.register(DoctorModel, DockAmin)
admin.site.register(PatientModel, patientAmin)
admin.site.register(AppointmentModel, AppointmentAdmin)
admin.site.register(DischargePatientModel, DischargedAdmin)
