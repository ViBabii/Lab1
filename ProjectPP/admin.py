from django.contrib import admin

from api.models import Doctors, Patients, Appointments, Declarations

# Register your models here.
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Appointments)
admin.site.register(Declarations)

