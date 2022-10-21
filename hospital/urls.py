import imp
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home_page"),
    path("doctorclick.html", views.HelloDoctView, name="hellodoct"),
    path("Doctor-Login", views.doctorLoginView.as_view(), name='doctor_login'),
    path("Doctor-Sogin", views.doctorsigninView.as_view(), name='doctor_signin'),
]
