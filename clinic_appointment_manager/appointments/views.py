from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# PATIENT
def login(request):
    return render(request, 'patient/login_patient.html')

def sign_patient(request):
    return render(request, 'patient/sign_patient.html')

def patient(request):
    return render(request, 'patient/patient_page.html')

def patient_form(request):
    return render(request, 'patient/patient_form.html')

    
# DOCTOR
def login_doctor(request):
    return render(request, 'doctor/login_doctor.html')

def doctor(request):
    return render(request, 'doctor/doctor_page.html')

def doctor_form(request):
    return render(request, 'doctor/doctor_form.html')