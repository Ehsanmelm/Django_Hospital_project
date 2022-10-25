from django import forms
from .models import PatientModel, DoctorModel

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
        fields = ["doctor", "is_accepted"]
