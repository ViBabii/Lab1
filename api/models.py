from django.db import models


class Declarations(models.Model):
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    patient = models.ForeignKey('Patients', models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'declarations'


class Doctors(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'doctors'


class Patients(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'patients'


class Appointments(models.Model):
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING, db_column='doctor_id')
    patient = models.ForeignKey('Patients', models.DO_NOTHING, db_column='patient_id')
    appointment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appointments'

