from django import forms
from .models import PatientModel, DoctorModel, AppointmentModel

# ------------ doctor related forms-------------


class DoctorSigninForm(forms.ModelForm):
    class Meta:
        model = DoctorModel
        fields = '__all__'
        exclude = ["status"]


class DoctorLoginForm(forms.ModelForm):
    class Meta:
        model = DoctorModel
        fields = ["Doct_name", "password"]


# ----------------------------------------------------------
# ----------------- patient related Forms ------------------
# ----------------------------------------------------------

class PatientSigninForm(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields = '__all__'
        exclude = ["doctor", "is_accepted", "is_discharged"]


class PatientLoginForm(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields = ["patient_name", "password"]


class DateInput(forms.DateInput):
    input_type = 'date'


class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = ['description', 'date']
        widgets = {
            'date': DateInput()
        }
