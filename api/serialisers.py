from rest_framework import serializers
from core import models

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username','password','email','role','address','contacts']

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            address=validated_data['address'],
            contacts=validated_data['contacts']
        )
        return user
    
class DoctorAppointmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'

class PatientHistorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalReport
        fields ='__all__'

class PatientHomepageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'

class AppointmentCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields =['doctor','notes']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['patient']=user
        return super().create(validated_data)