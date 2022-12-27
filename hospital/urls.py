from . import views
from django.urls import path
# ---------------------- Doctor ------------------------
urlpatterns = [
    path("", views.index, name="home_page"),
    path("doctorclick.html", views.HelloDoctView, name="hellodoct"),
    path("Doctor-Login", views.doctorLoginView.as_view(), name='doctor_login'),
    path("Doctor-Signin", views.doctorsigninView.as_view(), name='doctor_signin'),
    path("Doctor-Dashboard", views.doctor_dashboard, name='doctor_dashboard'),
]

# ---------------------- Doctor appointment ------------------------
urlpatterns += [
    path("Doctor-appointment", views.doctor_appointment_view,
         name='doctor_appointment'),
    path("Doctor-view-Appointments", views.doctor_view_appointment_view,
         name='doctor_view_appointment'),
    path("Check-Appointment", views.check_appointment_View,
         name='check_appointment'),
    path("Delete-Appointment/<int:pk>",
         views.delete_appointment,  name='deleting_appointment'),
    path('Accept-Appointment/<int:pk>', views.accept_appointment_view,
         name='accept_appointment')
]
# ---------------------- Doctor-patient ------------------------

urlpatterns += [
    path("Doctor-Patient", views.doctor_patient, name='doctor_patient'),
    path("Doctor-View-Patient", views.doctor_view_patient,
         name='doctor_view_patient'),
]

# ---------------------- Discharging-Patient ------------------------

urlpatterns += [
    path("Discharge-patient", views.Discharging_patint_view,
         name='discharge_patient'),
    path("Discharge-Process/<int:pk>",
         views.discharge_process_view.as_view(), name="discharge_process"),
    path("Download-Bill/<int:code>", views.download_pdf_view, name='download_bill'),
    path("View-Discharged-patient", views.view_discharged_patient_view,
         name='view_discharged_patient'),
]
# ---------------------- patinet ------------------------
urlpatterns += [
    path("Patient-Click", views.PatientClick, name='patient_click'),
    path("Patient-Signin", views.patientsigninView.as_view(), name='patient_signin'),
    path("Patient-Login", views.patientLoginView.as_view(), name='patient_login'),
    path("Patient-Dashboard", views.patient_dashboard, name='patient_dashboard'),
]

# -------------------------- paitent appointment ------------------------
urlpatterns += [
    path("Appointment", views.appointment, name='appointment'),
    path("Book-Appointment", views.BookAppointmentView.as_view(),
         name='book_appointment'),
    path("View-Appointment", views.pattinetViewAppointment,
         name='view_appointment'),
]

# -------------------------- paitent View Discharge Bill ------------------------

urlpatterns += [
    path("View_Discharge_Bill", views.Patient_View_Bill,
         name='view_discharged_bill')
]
