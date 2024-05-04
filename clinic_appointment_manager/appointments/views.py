from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import AppointmentForm

# Create your views here.
# PATIENT
def login_user(request):
    if request.method == 'GET':
        return render(request, 'patient/login_patient.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'patient/login_patient.html', {
                "error": "Username or password is incorrect."
                })
            
        else:
            login(request, user)
            return redirect('patient/')

def sign_patient(request):
    
    if request.method == 'GET':
        return render(request, 'patient/sign_patient.html')
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'],
                                                last_name=request.POST['lastname'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                #birthdate=request.POST['birthdate'],
                                                #home_address=request.POST['address'],
                                                #phone_number=request.POST['phone'],
                                                #weight=request.POST['weight'],
                                                #height=request.POST['height'],
                                                #gender=request.POST['gender']
                                                )
            user.save()
            print(user)
            print('User created successfully')   
            login(request, user)
            return redirect ('/patient/')
        except IntegrityError:
            return render(request, 'patient/sign_patient.html', {
                "error": 'Username already exists.'
            })
        
        
    

def patient(request):
    return render(request, 'patient/patient_page.html')

def patient_form(request):
    return render(request, 'patient/patient_form.html', {
        'form': AppointmentForm
    })

def patient_profile(request):
    return render(request, 'patient/patient_profile.html')
    
def logout_user(request):
    logout(request)
    return redirect('/')
    
###############################    
# DOCTOR
def login_doctor(request):
    return render(request, 'doctor/login_doctor.html')

def doctor(request):
    return render(request, 'doctor/doctor_page.html')

def doctor_form(request):
    return render(request, 'doctor/doctor_form.html')