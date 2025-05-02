from django.db import models
from django.contrib.auth.models import AbstractUser

# I am keeping the database design same for both apps so there will only be one Model

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('patient','Patient')
    ]
    photo = models.ImageField(upload_to='user/')
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300)
    contacts = models.IntegerField()
    role = models.CharField(max_length=30,choices=ROLE_CHOICES)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','address','contacts']

    def __str__(self):
        return f"({self.role})-{self.username}"
    
class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    specialization = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user} as doctor"

class Patient(models.Model):
    Gender_choices = [
        ('male','Male'),
        ('female','Female')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=30,choices=Gender_choices)

    def __str__(self):
        return f"{self.user} as patient"

class Appointment(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctors_patient")
    appointment_date =models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.patient}'s appointment with {self.doctor} on {self.appointment_date}"

class MedicalReport(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)
    diagonosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Report of {self.appointment}"

