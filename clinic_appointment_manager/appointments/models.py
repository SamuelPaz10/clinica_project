from django.db import models


### REVISAR LOS NUEVOS CAMPOS Y LOS TIPOS DE DATOS
class Patient(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    home_address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    weight = models.DecimalField()
    height = models.DecimalField()
    gender = models.TextChoices("Male", "Female")
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    status = models.CharField(max_length=20, choices=gender_choices, default='Males')
    # Agregar más campos según sea necesario

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    available_hours = models.JSONField()
    available_days = models.JSONField()
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
