import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from darmankade_app.forms import PatientForm, UserForm, DoctorForm
from darmankade_app.models import Patient, User, Doctor


def home(request):
    """
    Showing home page of site
    """
    return render(request, "home.html")


def patient_register(request):
    """
    This function send a form and get it from patient to register him.
    If form is valid user Patient creates
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)
        if patient_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('patient_panel')
    else:
        user_form = UserForm()
        patient_form = PatientForm()
    return render(request, "patient_register.html",
                  {'user_form': user_form, 'patient_form': patient_form, 'register_or_change': 'register'})


def patient_login(request):
    """
    This function send a form and get it from patient to login him.
    If form is valid Patient will be logged in
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('patient_panel')
        else:
            if 'username' in user_form.errors.keys():
                del user_form.errors['username']
            user_form.add_error('username', 'username or password is not correct!')
    else:
        user_form = UserForm()
    return render(request, "patient_login.html",
                  {'user_form': user_form})


@login_required(login_url='/patient_register')
def patient_panel(request):
    return render(request, 'patient_panel.html', {'user': request.user})


def patient_change_infos(request):
    """
    This function send a form and get it from patient to change his infos.
    If form is valid patients infos will be changed
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        patient_form = PatientForm(data=request.POST)
        username = request.POST.get("username")

        # These lines are used when user write old username in changing user info form
        if request.user.username == username:
            del user_form.errors['username']
        phone_number = request.POST.get("phone_number")
        patient = request.user.patient
        if patient.phone_number == phone_number:
            del patient_form.errors['phone_number']

        if patient_form.is_valid() and user_form.is_valid():
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


def medical_specialties(request):
    return render(request, "medical_specialties.html")


def neorologist(request):
    return render(request, "neorologist.html")


def dedicated_doctor_page(request, id):
    doctor = Doctor.objects.get(id=id)
    return render(request, "dedicated_doctor_page.html", {'doctor': doctor})


######## Doctor section ############


def doctor_register(request):
    """
    This function send a form and get it from doctor to register him.
    If form is valid user Doctor creates
    """
    if request.method == 'POST':

        # print("files:")

        # week_days = {day: day in request.POST for day in ['saturday', 'sunday', 'monday', 'tuesday',
        #                                                   'wednesday', 'thursday', 'friday']}
        # print(week_days)
        user_form = UserForm(data=request.POST)
        doctor_form = DoctorForm(request.POST, request.FILES)
        # print(user_form.errors)
        # print(doctor_form.errors)
        if doctor_form.is_valid() and user_form.is_valid():
            print(doctor_form)
            user = user_form.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user
            week_days = {day: day in request.POST for day in ['saturday', 'sunday', 'monday', 'tuesday',
                                                              'wednesday', 'thursday', 'friday']}
            doctor.week_days = str(week_days)
            doctor.photo = doctor_form.cleaned_data.get('photo')
            doctor.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('doctor_panel')
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()
    return render(request, "doctor_register.html",
                  {'user_form': user_form, 'doctor_form': doctor_form, 'register_or_change': 'register'})


def doctor_login(request):
    """
    This function send a form and get it from patient to login him.
    If form is valid Patient will be logged in
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('doctor_panel')
        else:
            if 'username' in user_form.errors.keys():
                del user_form.errors['username']
            user_form.add_error('username', 'username or password is not correct!')
    else:
        user_form = UserForm()
    return render(request, "patient_login.html",
                  {'user_form': user_form})


@login_required(login_url='/doctor_register')
def doctor_panel(request):
    return render(request, 'doctor_panel.html', {'user': request.user})


def doctor_change_infos(request):
    """
    This function send a form and get it from patient to change his infos.
    If form is valid patients infos will be changed
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        doctor_form = DoctorForm(request.POST, request.FILES)
        username = request.POST.get("username")

        # These lines are used when user write old username in changing user info form
        if request.user.username == username:
            del user_form.errors['username']
        phone_number = request.POST.get("phone_number")
        doctor = request.user.doctor
        # print(request.FILES['photo'])
        if doctor.phone_number == phone_number:
            del doctor_form.errors['phone_number']

        # if 'phone_number' in doctor_form.errors.keys() and 'Doctor with this Phone number already exists.' in \
        #         doctor_form.errors['phone_number']:
        #     doctor_form.errors['phone_number'].remove('Doctor with this Phone number already exists.')
        print(request.POST)
        if doctor_form.is_valid() and user_form.is_valid():
            user = request.user
            user.username = username
            user.set_password = doctor_form.cleaned_data.get("password1")
            doctor.name = doctor_form.cleaned_data.get("name")
            doctor.speciality = doctor_form.cleaned_data.get("speciality")
            doctor.address = doctor_form.cleaned_data.get("address")
            doctor.doctor_number = doctor_form.cleaned_data.get("doctor_number")
            doctor.experience_year = doctor_form.cleaned_data.get("experience_year")
            doctor.online_payment = doctor_form.cleaned_data.get("online_payment")
            doctor.photo = doctor_form.cleaned_data.get('photo')
            doctor.phone_number = phone_number
            week_days = {day: day in request.POST for day in ['saturday', 'sunday', 'monday', 'tuesday',
                                                              'wednesday', 'thursday', 'friday']}
            doctor.week_days = str(week_days)
            doctor.save()
            user.save()

            auth_user = authenticate(username=user.username, password=user.password)
            login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('doctor_panel')
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()
    return render(request, "doctor_register.html",
                  {'user_form': user_form, 'doctor_form': doctor_form, 'register_or_change': 'change'})


def get_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    stars = doctor.stars.all()
    scores = [star.score for star in stars]
    if scores:
        rate = sum(scores) / len(scores)
    else:
        rate = 0
    if rate - int(rate) > 0.5:
        stars = int(rate) + 1
    else:
        stars = int(rate)
    comment = doctor.commets.all()[0]
    print(doctor.week_days.replace(' False,', '"False",').replace(' True,', '"True",').replace('\'', '"'))
    week_days = json.loads(doctor.week_days.replace(' False,', '"False",').replace(' True,', '"True",'))
    data = {
        'id': doctor.id,
        'name': doctor.name,
        'spec': doctor.speciality,
        'avatar': doctor.photo,
        'number': doctor.doctor_number,
        'online_pay': doctor.online_payment,
        'first_empty_date': '30 آذر',  ###؟؟؟؟؟؟؟؟؟
        'experience_years': doctor.experience_year,
        'stars': stars,
        'rate': rate,
        'commenter': comment.patient.user.username,
        'comments': len(doctor.commets),
        'comment_text': comment.text,
        'address': doctor.address,
        'phone': doctor.phone_number,
        'week_days': [week_days[day] for day in ['saturday', 'sunday', 'monday', 'tuesday',
                                                 'wednesday', 'thursday', 'friday']],
    }
    JsonResponse(data)


#######################################
def get_all_doctors(request):
    # TODO: doctor.name has only doctor's lastname
    doctors = Doctor.objects.all()
    data = []
    q = request.GET.get('q', '')
    for doctor in doctors:
        if not ((q in doctor.name) or (q in doctor.speciality) or (q in doctor.address)):
            continue
        scores = list(map(lambda x: x.score, doctor.stars.all()))
        print(scores)
        rate = 0 if (len(scores) == 0) else (sum(scores) / len(scores))
        print(rate)
        stars = int(rate) if (rate - int(rate) < 0.5) else (int(rate) + 1)
        comment = '---' if len(doctor.commets.all()) == 0 else doctor.commets.all()[0].text
        data.append({
            'id': doctor.id,
            'name': doctor.name,
            'spec': doctor.speciality,
            'avatar': doctor.photo.url,
            'stars': stars,
            'comments': len(doctor.commets.all()),
            'comment_text': comment,
            'location': '---',
            'experience_years': doctor.experience_year,
            'user_percent': rate,
            'first_empty_date': '30 آذر',  # ؟؟؟؟؟؟؟؟؟
        })
    return JsonResponse(data, safe=False)


def search_doctors(request):
    pass


def add_comment(request):
    pass


def rate_to_doctor(request):
    pass
