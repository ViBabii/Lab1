from rest_framework import serializers
from api.models import Declarations, Doctors, Patients, Appointments


class DeclarationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declarations
        fields = "__all__"


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"
