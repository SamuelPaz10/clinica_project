from django.db import models
from django.contrib.auth.models import User


### REVISAR LOS NUEVOS CAMPOS Y LOS TIPOS DE DATOS
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default="1234")
    birthdate = models.DateField()
    home_address = models.TextField()
    phone_number = models.CharField(max_length=20)
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=20, choices=gender_choices, default='Males')
    # Agregar más campos según sea necesario

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default="1234")
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    
    # Agregar más campos según sea necesario

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status_choices = (
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Scheduled')
    # Agregar más campos según sea necesario

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.date} {self.time} - {self.status}"
