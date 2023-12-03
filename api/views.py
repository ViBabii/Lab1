from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Declarations, Doctors, Patients
from api.serializers import DoctorsSerializer, PatientsSerializer, DeclarationsSerializer, AppointmentsSerializer


class PatientDoctorView(APIView):
    """
    View to get the doctor for a given patient.
    """
    def get(self, request, patient_id):
        try:
            declaration = Declarations.objects.get(patient_id=patient_id)
            doctor = declaration.doctor
            serializer = DoctorsSerializer(doctor)
            return Response(serializer.data)
        except Declarations.DoesNotExist:
            return Response({"error": "Declaration not found"}, status=status.HTTP_404_NOT_FOUND)


class DoctorPatientsView(APIView):
    """
    View to get all patients for a given doctor.
    """
    def get(self, request, doctor_id):
        declarations = Declarations.objects.filter(doctor_id=doctor_id)
        patients = [declaration.patient for declaration in declarations]
        serializer = PatientsSerializer(patients, many=True)
        return Response(serializer.data)


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


class DeclarationCreateView(APIView):
    """
    View to create a new declaration with a new patient and an existing doctor.
    """

    def post(self, request):
        # Deserialize patient data
        patient_serializer = PatientsSerializer(data=request.data.get('patient'))
        if patient_serializer.is_valid():
            # Save new patient
            patient = patient_serializer.save()
        else:
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if doctor exists
        doctor_id = request.data.get('doctor_id')
        try:
            doctor = Doctors.objects.get(id=doctor_id)
        except Doctors.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create and save the declaration
        declaration_data = {
            'doctor': doctor.id,
            'patient': patient.id,
            'date': request.data.get('date')
        }
        declaration_serializer = DeclarationsSerializer(data=declaration_data)

        if declaration_serializer.is_valid():
            with transaction.atomic():
                declaration_serializer.save()
            return Response(declaration_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(declaration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentCreateView(APIView):
    """
    View to create a new appointment.
    """
    def post(self, request):
        # Deserialize appointment data
        appointment_serializer = AppointmentsSerializer(data=request.data)
        if appointment_serializer.is_valid():
            # Save new appointment
            appointment_serializer.save()
            return Response(appointment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
