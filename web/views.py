from django.shortcuts import render

# Create your views here.

def doctorhomepage(request):
    return render(request,'doctor_homepage.html')


def login_view(request):
    return render(request, 'login.html')