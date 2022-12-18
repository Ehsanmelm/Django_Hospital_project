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
