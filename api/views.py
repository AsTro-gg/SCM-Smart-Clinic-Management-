from django.shortcuts import render
from rest_framework import generics
from core.models import *
from .serialisers import *
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'role': user.role}, status=status.HTTP_200_OK)

class DoctorHomepage(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = DoctorAppointmentSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role !='doctor':
            return Appointment.objects.none()
        return Appointment.objects.filter(doctor=user)

        
class DoctorAppointmentCompleted(generics.GenericAPIView):
    queryset = Appointment.objects.all()
    permission_classes =[IsAuthenticated]
    
    def delete(self, request,pk, *args, **kwargs):
        if request.user.role != 'doctor':
            return Response({'Unauthorized':'You are not authorized'},status=status.HTTP_403_FORBIDDEN)
        deleting_object = get_object_or_404(Appointment,id=pk)

        if deleting_object.doctor != request.user:
            return Response({'Unauthorized':'This is not your Appointment'},status=status.HTTP_403_FORBIDDEN)
        
        deleting_object.delete()
        return Response({"Deleted":"No Content"},status=status.HTTP_204_NO_CONTENT)
    
class BasePatientHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        """
        This method will be overridden in child classes.
        By default, returns all medical reports.
        """
        return MedicalReport.objects.all()

    def get(self, request, pk=None):
        """
        Base method for fetching patient history.
        This method can be inherited and overridden.
        """
        queryset = self.get_queryset(pk)
        serializer = PatientHistorySerialiser(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorPatientHistoryView(BasePatientHistoryView):
    def get_queryset(self, pk):
        """
        For the doctor, show all medical reports for the specified patient.
        """
        return MedicalReport.objects.filter(appointment__patient__id=pk)
    

class PatientHistoryView(BasePatientHistoryView):
    def get_queryset(self,pk):
        return MedicalReport.objects.filter(appointment__patient__id=self.request.user.id)

# In doctor i need dynamic url because i want to get the reports of the patient which is selected or searched for but 
#patients can only see their own. so no dynamic url

class PatientHomepage(generics.ListAPIView):
    queryset =  Doctor.objects.all()
    serializer_class = PatientHomepageSerialiser
    permission_classes = [IsAuthenticated]

class Appointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerialiser
    permission_classes =[IsAuthenticated]

# need to add more permission and control by customising the methods 
# only patients can make appointments , to only doctors , if doctors have 5 appointments no more appointments can  be made try again tommorow
# Also figure out how to delete all appointments automatically in 24 hours 
# send medical report as a pdf calling it prescribtion in the user's email
 
 ### minimum tasks for tommorow.