from django.contrib import admin
from .models import DoctorModel, PatientModel, AppointmentModel, DischargePatientModel, FeedBack_Model
# Register your models here.


class DockAmin(admin.ModelAdmin):
    list_display = ["Doct_name", "status"]


class patientAmin(admin.ModelAdmin):
    list_display = ["patient_name", "is_accepted"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name']


class DischargedAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'assigned_doctor_name']


class FeedBack_Admin(admin.ModelAdmin):
    list_display = ["name", "email"]


admin.site.register(DoctorModel, DockAmin)
admin.site.register(PatientModel, patientAmin)
admin.site.register(AppointmentModel, AppointmentAdmin)
admin.site.register(DischargePatientModel, DischargedAdmin)
admin.site.register(FeedBack_Model, FeedBack_Admin)
