import re
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import DoctorModel, PatientModel, AppointmentModel, DischargePatientModel, FeedBack_Model
from .forms import DoctorLoginForm, DoctorSigninForm, PatientSigninForm, PatientLoginForm, BookAppointmentForm, FeedBack_Form
from datetime import date
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
            valid_doctor = DoctorModel.objects.values(
                "Doct_name", "password", "status")
            for i in valid_doctor:
                if i["Doct_name"] == form.cleaned_data['Doct_name'] and i["password"] == form.cleaned_data['password']:
                    if i["status"]:
                        loged_in_doctor = DoctorModel.objects.get(
                            Doct_name=i["Doct_name"], password=i["password"])
                        request.session["loged_Doctor_id"] = loged_in_doctor.id
                        return HttpResponseRedirect(reverse('doctor_dashboard'))
                    else:
                        return render(request, "hospital/doctor_wait_for_approval.html", {"doct_name": i["Doct_name"]})
            else:
                return render(request, "hospital/doctor_login_error.html", {"doct_name": form.cleaned_data['Doct_name']})


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
            else:
                signin_form = form.save(commit=False)
                signin_form.status = False
                signin_form.save()
                login_form = DoctorLoginForm()
                return HttpResponseRedirect(reverse('doctor_login'))

        return render(request, "hospital/doctorsignup.html", {"form": form})


def doctor_dashboard(request):
    loged_doctor_id = request.session.get("loged_Doctor_id")
    loged_doctor = DoctorModel.objects.get(id=loged_doctor_id)
    contex = {
        'appointment': len(AppointmentModel.objects.filter(doctor_name=loged_doctor.Doct_name, doctor_pass=loged_doctor.password)),
        'patients': PatientModel.objects.filter(doctor__Doct_name=loged_doctor.Doct_name).count(),
        'discharged_count': DischargePatientModel.objects.filter(assigned_doctor_id=loged_doctor_id).count()
    }
    recent_appointment = AppointmentModel.objects.filter(
        doctor_name=loged_doctor.Doct_name, doctor_pass=loged_doctor.password).order_by('-date')[:3]
    # print(recent_appointment)

    patient_info = []
    for i in recent_appointment:
        patient_info.append(PatientModel.objects.get(
            patient_name=i.patient_name, password=i.patient_pass))
    # print(patient_info)
    appointment = zip(recent_appointment, patient_info)
    return render(request, "hospital/doctor_dashboard.html", {"contex": contex, "appointment": appointment})


def doctor_appointment_view(request):
    return render(request, 'hospital/doctor_appointment.html')


def doctor_view_appointment_view(request):
    loged_doctor_id = request.session.get("loged_Doctor_id")
    loged_doctor = get_object_or_404(DoctorModel, id=loged_doctor_id)
    appointments = AppointmentModel.objects.filter(
        doctor_name=loged_doctor.Doct_name, doctor_pass=loged_doctor.password, status=True).order_by('-date')
    patinets_id = []
    for i in appointments:
        patinets_id.append(PatientModel.objects.get(
            patient_name=i.patient_name, password=i.patient_pass))
    appointments_info = zip(appointments, patinets_id)

    return render(request, 'hospital/doctor_view_appointment.html', {"appointments_info": appointments_info})


def check_appointment_View(request):
    loged_doctor_id = request.session.get("loged_Doctor_id")
    loged_doctor = get_object_or_404(DoctorModel, id=loged_doctor_id)
    appointments = AppointmentModel.objects.filter(
        doctor_name=loged_doctor.Doct_name, doctor_pass=loged_doctor.password, status=False)
    patinets_id = []
    for i in appointments:
        patinets_id.append(PatientModel.objects.get(
            patient_name=i.patient_name, password=i.patient_pass))
    appointments_info = zip(appointments, patinets_id)
    return render(request, 'hospital/doctor_delete_appointment.html', {"appointments_info": appointments_info})


def delete_appointment(request, pk):
    appointment = AppointmentModel.objects.get(id=pk)
    appointment.delete()
    return HttpResponseRedirect(reverse('check_appointment'))


def accept_appointment_view(request, pk):
    appointment = AppointmentModel.objects.get(id=pk)
    appointment.status = True
    appointment.save()
    return HttpResponseRedirect(reverse('check_appointment'))


def doctor_patient(request):
    return render(request, "hospital/doctor_patient.html")


def doctor_view_patient(request):
    doct_id = request.session.get('loged_Doctor_id')
    doctor = get_object_or_404(DoctorModel, id=doct_id)
    patient_list = PatientModel.objects.filter(
        doctor=doct_id, is_discharged=False)
    # print(patient_list[0].mobile)
    return render(request, "hospital/doctor_view_patient.html", {'patient_list': patient_list})


def Discharging_patint_view(request):
    loged_doctor_id = request.session.get("loged_Doctor_id")
    doctor = get_object_or_404(DoctorModel, id=loged_doctor_id)
    not_discharged_patinet = PatientModel.objects.filter(
        doctor__Doct_name=doctor.Doct_name, doctor__password=doctor.password, is_discharged=False)
    return render(request, "hospital/doctor_discharge_patient.html", {"patients": not_discharged_patinet})


class discharge_process_view(View):

    def get(self, request, pk):
        discharging_patient = get_object_or_404(PatientModel, id=pk)
        assigned_doctor = request.session.get("loged_Doctor_id")

        discharge_form = DischargePatientModel(patient_name=discharging_patient.patient_name, patient_pass=discharging_patient.password, todaydate=date.today(),
                                               assigned_doctor_name=discharging_patient.doctor, mobile=discharging_patient.mobile, address=discharging_patient.address, symptoms=discharging_patient.symptoms, assigned_doctor_id=assigned_doctor, profile_pic=discharging_patient.profile_pic)
        discharge_form.save()
        return render(request, 'hospital/patient_generate_bill.html', {"discharge_form": discharge_form})

    def post(self, request, pk):
        patient = get_object_or_404(PatientModel, id=pk)
        discharging_patient = DischargePatientModel.objects.get(
            patient_name=patient.patient_name, patient_pass=patient.password)
        # print(discharging_patient.mobile)
        discharging_patient.patient_code = pk
        total_price = 0
        total_price += int(request.POST['roomCharge'])
        discharging_patient.roomCharge = int(request.POST['roomCharge'])

        total_price += int(request.POST['medicineCost'])
        discharging_patient.medicineCost = int(request.POST['medicineCost'])

        total_price += int(request.POST['doctorFee'])
        discharging_patient.doctorFee = int(request.POST['doctorFee'])

        total_price += int(request.POST['OtherCharge'])
        discharging_patient.OtherCharge = int(request.POST['OtherCharge'])
        discharging_patient.total_price = total_price
        patient.is_discharged = True
        patient.save()
        discharging_patient.save()

        return render(request, "hospital/patient_final_bill.html", {"discharging_patient": discharging_patient})


def download_pdf_view(request, code):
    print(id)
    discharge_pdf_info = DischargePatientModel.objects.get(
        patient_code=code)
    return render(request, "hospital/download_bill.html", {"discharge_pdf_info": discharge_pdf_info})


def view_discharged_patient_view(request):
    loged_doct_id = request.session.get("loged_Doctor_id")
    discharged_patient_list = DischargePatientModel.objects.filter(
        assigned_doctor_id=loged_doct_id)
    return render(request, "hospital/doctor_view_discharge_patient.html", {"discharged_patient_list": discharged_patient_list})

    # ----------------------------------------------------------
    # ----------------- patient related ------------------------
    # ----------------------------------------------------------


def Patient_View_Bill(request):
    loged_patient_id = request.session.get("loged_patient_id")
    try:
        dischrge_bill_info = DischargePatientModel.objects.get(
            patient_code=loged_patient_id)
        discharge_status = True
    except:
        dischrge_bill_info = []
        # discharge_status = PatientModel.objects.get(
        #     id=loged_patient_id).is_discharged
        discharge_status = False
    return render(request, 'hospital/patient_discharge.html', {"Bill": dischrge_bill_info, "is_discharged": discharge_status})


def PatientClick(request):
    return render(request, "hospital/patientclick.html")


class patientsigninView(View):
    def get(self, request):
        form = PatientSigninForm()
        return render(request, "hospital/patientsignup.html", {"form": form})

    def post(self, request):
        form = PatientSigninForm(request.POST)
        print(form.errors)
        if form.is_valid():
            patients = PatientModel.objects.values(
                "patient_name", "password", "email")
            for i in patients:
                if (i["patient_name"] == form.cleaned_data['patient_name'] and i["password"] == form.cleaned_data['password']) or i["email"] == form.cleaned_data['email']:
                    return render(request, "hospital/patientsignup.html", {"form": form, "msg": "There is a same Doctor with same  Account !"})
            else:
                form.save()
                return HttpResponseRedirect(reverse('patient_login'))
        return render(request, "hospital/patientsignup.html", {"form": form})


class patientLoginView(View):
    def get(self, request):
        form = PatientLoginForm()
        return render(request, "hospital/patientlogin.html", {"form": form})

    def post(self, request):
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            accepted_patient = PatientModel.objects.values(
                "patient_name", "password", "is_accepted")
            for i in accepted_patient:
                if i['patient_name'] == form.cleaned_data['patient_name'] and i['password'] == form.cleaned_data['password']:
                    if i["is_accepted"]:
                        # return HttpResponseRedirect(reverse('patient_dashboard'))
                        loged_in_patient = PatientModel.objects.get(
                            patient_name=i["patient_name"], password=i["password"])
                        patient_related_doct = DoctorModel.objects.get(
                            Doct_name=loged_in_patient.doctor)
                        request.session["loged_patient_id"] = loged_in_patient.id
                        return HttpResponseRedirect(reverse('patient_dashboard'))

                    else:
                        return render(request, "hospital/patient_wait_for_approval.html", {"patient_name": i['patient_name']})
            else:
                return render(request, "hospital/patient_login_error.html")


def patient_dashboard(request):
    loged_patient_id = request.session.get("loged_patient_id")
    print(loged_patient_id)
    loged_in_patient = get_object_or_404(PatientModel, id=loged_patient_id)
    related_doct_patient = get_object_or_404(
        DoctorModel, Doct_name=loged_in_patient.doctor)
    return render(request, "hospital/patient_dashboard.html", {"loged_in_patient": loged_in_patient, "patient_related_doct": related_doct_patient})


def appointment(request):
    return render(request, 'hospital/patient_appointment.html')


class BookAppointmentView(View):
    def get(self, request):
        form = BookAppointmentForm()
        return render(request, 'hospital/patient_book_appointment.html', {'form': form})

    def post(self, request):
        form = BookAppointmentForm(request.POST)
        loged_in_patient_id = request.session.get("loged_patient_id")
        loaged_patinet = get_object_or_404(
            PatientModel, id=loged_in_patient_id)
        related_docter = get_object_or_404(
            DoctorModel, Doct_name=loaged_patinet.doctor)

        appointment = AppointmentModel(patient_name=loaged_patinet.patient_name, doctor_name=related_docter.Doct_name,
                                       patient_pass=loaged_patinet.password, doctor_pass=related_docter.password,  description=request.POST.get('description'), date=request.POST.get('date'))
        appointment.save()
        return HttpResponseRedirect(reverse('appointment'))


def pattinetViewAppointment(request):
    loged_in_patient_id = request.session.get("loged_patient_id")
    loged_patient = get_object_or_404(PatientModel, id=loged_in_patient_id)
    appointments = AppointmentModel.objects.filter(
        patient_name=loged_patient.patient_name, patient_pass=loged_patient.password)
    return render(request, 'hospital/patient_view_appointment.html', {"appointments": appointments})


# --------------------------------------------- FeedBack ---------------------------------------------

class FeedBack_View(View):
    def get(self, request):
        form = FeedBack_Form()
        return render(request, "hospital/feedback.html", {"form": form})

    def post(self, request):
        form = FeedBack_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "hospital/feedbackssuccess.html", {"form": form})

        return render(request, "hospital/feedback.html", {"form": form})
