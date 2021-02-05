from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from darmankade_app.forms import PatientForm, UserForm, DoctorForm
from darmankade_app.models import Patient


def home(request):
    return render(request, "home.html")


def patient_register(request):
    if request.method == 'POST':
        # print(request.POST)
        user_form = UserForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)
        if patient_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()

            # print('patient saved')
            # auth_user = authenticate(username=user.username,
            #                          password=user.password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('patient_panel')
    else:
        user_form = UserForm()
        patient_form = PatientForm()
    return render(request, "patient_register.html",
                  {'user_form': user_form, 'patient_form': patient_form, 'register_or_change': 'register'})


def patient_login(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)
        if patient_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()

            # print('patient saved')
            # auth_user = authenticate(username=user.username,
            #                          password=user.password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('patient_panel')
    else:
        user_form = UserForm()
        patient_form = PatientForm()
    return render(request, "patient_login.html",
                  {'user_form': user_form, 'patient_form': patient_form})



@login_required(login_url='/patient_register')
def patient_panel(request):
    # print(request.user.username)
    # try:
    #     patient = Patient.objects.get(user=request.user)
    # except:
    #     patient = request.user
    return render(request, 'patient_panel.html', {'user': request.user})


def patient_change_infos(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)
        username = request.POST.get("username")

        # These lines are used when user write old username in changing user info form
        if request.user.username == username:
            del user_form.errors['username']
        phone_number = request.POST.get("phone_number")
        # patient = Patient.objects.get(username=request.user.username)
        patient = request.user.patient
        if patient.phone_number == phone_number:
            del user_form.errors['phone_number']

        if patient_form.is_valid():
            user = request.user
            user.username = username
            user.set_password = patient_form.cleaned_data.get("password1")
            patient.phone_number = patient_form.cleaned_data.get("phone_number")
            patient.save()
            user.save()

            auth_user = authenticate(username=user.username,
                                     password=user.password)
            login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('patient_panel')
    else:
        user_form = UserForm()
        patient_form = PatientForm()
    return render(request, "patient_register.html",
                  {'user_form': user_form, 'patient_form': patient_form, 'register_or_change': 'change'})
