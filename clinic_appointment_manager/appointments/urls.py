#<<<<<<< HEAD
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
#=======
from django.urls import path
from . import views]

urlpatterns = [
    path('', views.login),
    path('patient/', views.patient),
    path('patient/form', views.patient_form),
    
    path('login_doctor', views.login_doctor),
    path('doctor/', views.doctor),
    path('doctor/form', views.doctor_form),
#>>>>>>> 6b4fc5b2396b2305acf1114df2b365c7cde28e86
]