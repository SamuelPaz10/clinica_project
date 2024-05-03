from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('patient/', views.patient),
    path('patient/sign', views.sign_patient),
    path('patient/form', views.patient_form),
    
    path('login_doctor', views.login_doctor),
    path('doctor/', views.doctor),
    path('doctor/form', views.doctor_form),
]