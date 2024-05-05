from django.db import models
from django.contrib.auth.models import User
import json

### REVISAR LOS NUEVOS CAMPOS Y LOS TIPOS DE DATOS
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, unique=True)
    last_name = models.CharField(max_length=100)
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
        #return self.user.username
        return f"{self.user.username} {self.last_name}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, unique=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    available_datetime = models.TextField(default='[]')
    
    def get_available_datetime(self):
        return json.loads(self.available_datetime)

    def agg_available_datetime(self, datetime):
        datetimes = self.get_available_datetime()
        datetimes.append(datetime)
        self.available_datetime = json.dumps(datetimes)
        self.save()

    def delete_available_datetime(self, datetime):
        datetimes = self.get_available_datetime()
        if datetime in datetimes:
            datetimes.remove(datetime)
            self.available_datetime = json.dumps(datetimes)
            self.save()
    # Agregar más campos según sea necesario

    def __str__(self):
        return f"{self.user.username} {self.last_name} - {self.specialization}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.TextField()
    available_datetimes = (
        ('Lun 01-05-2024/10:00', 'Lun 01-05-2024/10:00'),
        ('Lun 01-05-2024/10:00', 'Lun 01-05-2024/10:00'),
        )
    available_datetime = models.CharField(max_length=20, choices=available_datetimes, default='Scheduled')
    status_choices = (
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Scheduled')
    # Agregar más campos según sea necesario

    def __str__(self):
        return f"{self.patient} || {self.doctor} || {self.status} || {self.available_datetime}"
