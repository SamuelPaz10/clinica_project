from django.forms import ModelForm
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'reason', 'available_datetime', 'status']