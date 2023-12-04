from django.db import transaction
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.forms import DoctorForm, PatientForm, AppointmentForm
from api.models import Doctors, Patients, Appointments
from api.serializers import DoctorsSerializer, PatientsSerializer, AppointmentsSerializer


class PatientDoctorView(APIView):
    """
    View to get the doctor for a given patient.
    """

    def get(self, request, patient_id):
        try:
            patient = Patients.objects.get(id=patient_id)
            doctor = patient.id_doctor
            serializer = DoctorsSerializer(doctor)
            return Response(serializer.data)
        except Patients.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)


class DoctorPatientsView(APIView):
    """
    View to get all patients for a given doctor.
    """

    def get(self, request, doctor_id):
        try:
            patients = Patients.objects.filter(id_doctor=doctor_id)
            serializer = PatientsSerializer(patients, many=True)
            return Response(serializer.data)
        except Doctors.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)


class PatientCreateView(APIView):
    """
    View to create a new patient.
    """

    def post(self, request):
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentCreateView(APIView):
    """
    View to create a new appointment.
    """

    def post(self, request):
        appointment_serializer = AppointmentsSerializer(data=request.data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return Response(appointment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'home.html')


def addDoctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DoctorForm()
    return render(request, 'addDoctor.html', {'form': form})


def addClient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'addClient.html', {'form': form})


def addAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'addAppointment.html', {'form': form})
