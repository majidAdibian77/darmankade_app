from django.shortcuts import render

# Create your views here.
from darmankade_app.forms import PatientForm
from darmankade_app.models import Patient


def home(request):
    return render(request, "home.html")


def patient_register(request):
    if request.method == 'POST':
        print(request.POST)
        patient_form = PatientForm(data=request.POST)
        if patient_form.is_valid():
            user = patient_form.save()
            return render(request, 'patient_panel.html')
    else:
        patient_form = PatientForm()
    return render(request, "patient_register.html",
                  {'form': patient_form})


def patient_login(request):
    return render(request, 'patient_login.html')
