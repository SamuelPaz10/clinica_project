from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
# PATIENT
def login(request):
    return render(request, 'patient/login_patient.html')

def sign_patient(request):
    
    if request.method == 'GET':
        return render(request, 'patient/sign_patient.html')
    else: 
        try:
            user = User.objects.create_user(username=request.POST['username'],
                                            lastname=request.POST['lastname'],
                                            email=request.POST['email'],
                                            password=request.POST['password'],
                                            birthdate=request.POST['birthdate'],
                                            address=request.POST['address'],
                                            phone=request.POST['phone'],
                                            weight=request.POST['weight'],
                                            height=request.POST['height'],
                                            gender=request.POST['gender'])
            user.save()
            print('User created successfully')   
            #return HttpResponse('User created successfully')
            return render(request, 'patient/patient_page.html')
        except:
            return HttpResponse('Username already exists')
    
    

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