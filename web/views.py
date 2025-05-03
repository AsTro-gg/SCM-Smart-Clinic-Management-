from django.shortcuts import render

# Create your views here.

def doctorhomepage(request):
    return render(request,'doctor_homepage.html')