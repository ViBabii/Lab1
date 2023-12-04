from django.db import models


class Doctors(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patients(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    id_doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.appointment_date} - {self.doctor} - {self.patient}"
