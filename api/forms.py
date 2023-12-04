from django import forms
from .models import Doctors, Patients, Appointments


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['first_name', 'last_name']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'last_name', 'id_doctor']
    labels = {
            'id_doctor': 'doctor'
    }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['doctor', 'patient', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }