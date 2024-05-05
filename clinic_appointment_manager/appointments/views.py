from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import AppointmentForm


# INICIAR SESIÓN
def login_user(request):
    if request.method == "GET":
        return render(request, "patient/login_patient.html")
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "patient/login_patient.html",
                {"error": "Username or password is incorrect."},
            )

        else:
            login(request, user)
            return redirect("patient/")


# REGISTRARSE
def sign_patient(request):

    if request.method == "GET":
        return render(request, "patient/sign_patient.html")
    else:
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                last_name=request.POST["lastname"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            user.save()
            print(user)
            print("User created successfully")
            login(request, user)
            return redirect("/patient/")
        except IntegrityError:
            return render(
                request,
                "patient/sign_patient.html",
                {"error": "Username already exists."},
            )


# CARGA LA PÁGINA PRINCIPAL
def patient(request):
    return render(request, "patient/patient_page.html")


# CARGA LA PÁGINA PARA AGENDAR CITAS
def appointments_create(request):
    if request.method == "GET":
        return render(
            request, 'patient/appointments_create.html', {'form': AppointmentForm}
        )
    else:
        form_appointments = AppointmentForm(request.POST)
        new_appointments = form_appointments.save(commit=False)
        new_appointments.user = request.user
        new_appointments.save()
        return redirect("/patient/")


def patient_profile(request):
    return render(request, "patient/patient_profile.html")


def logout_user(request):
    logout(request)
    return redirect("/")


###############################
# DOCTOR
def login_doctor(request):
    return render(request, "doctor/login_doctor.html")


def doctor(request):
    return render(request, "doctor/doctor_page.html")


def doctor_form(request):
    return render(request, "doctor/doctor_form.html")
