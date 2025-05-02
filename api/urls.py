from django.urls import path
from .views import *
urlpatterns = [
    # login and register
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',login,name='login'),
    

    # Doctor Homepage
    path('doctor-appointment/',DoctorHomepage.as_view(),name='DoctorHomepage'),
    path('doctor-appointment-completed/<int:pk>/',DoctorAppointmentCompleted.as_view(),name='DoctorAppointmentComplete'),
    path('doctor-patient-history/<int:pk>/',DoctorPatientHistoryView.as_view(),name='DoctorPatientHistory'),

    #Patient Homepage  
    path('patient-homepage/',PatientHomepage.as_view(),name='PatientHomepage'),
    path('patient-history/',PatientHistoryView.as_view(),name='PatientHistory'),


]