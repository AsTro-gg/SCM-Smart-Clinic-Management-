from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/homepage/',doctorhomepage,name='doctorhomepage'),
]