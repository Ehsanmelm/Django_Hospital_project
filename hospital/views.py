import re
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import DoctorModel, PatientModel
from .forms import DoctorLoginForm, DoctorSigninForm, PatientSigninForm

# Create your views here.


def index(request):
    return render(request, "hospital/index.html")


def HelloDoctView(request):
    return render(request, 'hospital/doctorclick.html')


class doctorLoginView(View):
    def get(self, request):
        form = DoctorLoginForm()
        return render(request, "hospital/doctorlogin.html", {"form": form})

    def post(self, request):
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            # try:
            #     search_doct = DoctorModel.objects.get(
            #         Doct_name=form.cleaned_data['Doct_name'], password=form.cleaned_data['password'])
            #     # print("<<<<<<<<<<<<<<hast")
            #     return render(request, "hospital/doctorlogin.html", {"form": form})
            # except:
            #     # print("nist>>>>>>>>>>>>>>>>")
            #     return render(request, "hospital/doctorsignin.html", {"form": form})
            valid_doctor = DoctorModel.objects.values(
                "Doct_name", "password", "status")
            for i in valid_doctor:
                if i["Doct_name"] == form.cleaned_data['Doct_name'] and i["password"] == form.cleaned_data['password']:
                    if i["status"]:
                        return HttpResponseRedirect(reverse('doctor_dashboard'))
                    else:
                        return render(request, "hospital/doctor_wait_for_approval.html", {"doct_name": i["Doct_name"]})
            else:
                return render(request, "hospital/doctor_login_error.html", {"doct_name": form.cleaned_data['Doct_name']})

        # return HttpResponseRedirect('hellodoct')


class doctorsigninView(View):
    def get(self, request):
        form = DoctorSigninForm()
        return render(request, "hospital/doctorsignup.html", {"form": form})

    def post(self, request):
        form = DoctorSigninForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['password'])
            doctors_list = DoctorModel.objects.values("Doct_name", "password")
            for i in doctors_list:
                if i["Doct_name"] == form.cleaned_data['Doct_name'] and i["password"] == form.cleaned_data['password']:
                    return render(request, "hospital/doctorsignup.html", {"msg": "There is a same Doctor with samea  Account !", "form": form})
                    # return HttpResponseRedirect(reverse('doctor_signin', args=[""]))
            else:
                signin_form = form.save(commit=False)
                signin_form.status = False
                signin_form.save()
                login_form = DoctorLoginForm()
                # return render(request, "hospital/doctorlogin.html")
                return HttpResponseRedirect(reverse('doctor_login'))

        return render(request, "hospital/doctorsignup.html", {"form": form})


def doctor_dashboard(request):
    return render(request, "hospital/doctor_dashboard.html")


# ----------------------------------------------------------
# ----------------- patient related ------------------------
# ----------------------------------------------------------

def PatientClick(request):
    return render(request, "hospital/patientclick.html")


class patientsigninView(View):
    def get(self, request):
        form = PatientSigninForm()
        return render(request, "hospital/patientsignup.html", {"form": form})

    def post(self, request):
        form = PatientSigninForm(request.POST)
        if form.is_valid():
            patients = PatientModel.objects.values("Patient_name", "password")
            for i in patients:
                if i["Patient_name"] == form.cleaned_data['Patient_name'] and i["password"] == form.cleaned_data['password']:
                    return render(request, "hospital/patientsignup.html", {"form": form, "msg": "There is a same Doctor with samea  Account !"})
            else:
                form.save()
            return


class doctorLoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# def patient_dashboard(request):
#     return render(request, "hospital/doctor_dashboard.html")
