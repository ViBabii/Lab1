"""
URL configuration for ProjectPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from api.views import PatientDoctorView, DoctorPatientsView, PatientCreateView, DeclarationCreateView, AppointmentCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('PatientDoctorView/<int:patient_id>', PatientDoctorView.as_view()),
    path('DoctorPatientsView/<int:doctor_id>', DoctorPatientsView.as_view()),
    path('PatientCreateView/', PatientCreateView.as_view()),
    path('DeclarationCreateView/', DeclarationCreateView.as_view()),
    path('AppointmentCreateView/', AppointmentCreateView.as_view()),
]

