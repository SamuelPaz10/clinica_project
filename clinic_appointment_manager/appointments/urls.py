from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('patient/', views.patient),
    path('patient/sign', views.sign_patient),
    path('appointments/schedule/', views.appointments_create),
    path('patient/profile', views.patient_profile),
    path('logout/', views.logout_user, ),
    
    path('login_doctor', views.login_doctor),
    path('doctor/', views.doctor),
    path('doctor/form', views.doctor_form),
]