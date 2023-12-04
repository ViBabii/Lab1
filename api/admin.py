from django.contrib import admin

from api.models import Doctors, Patients, Appointments

# Register your models here.
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Appointments)

