from django.conf.urls import url
from darmankade_app import views
from django.contrib.auth import views as djangoView

# from meeting_app.views import OAuth2CallBack

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^medical_specialties$', views.medical_specialties, name="medical_specialties"),
    url(r'^neurologist$', views.neorologist, name="neorologist"),
    url(r'^dedicated_doctor_page$', views.dedicated_doctor_page, name="dedicated_doctor_page"),

    url(r'^user_login$', views.user_login, name="user_login"),
    # url(r'^user_logout$', views.user_logout, name="user_logout"),
    url(r'^user_logout/$', djangoView.LogoutView.as_view(), name="user_logout"),

    url(r'^patient_register$', views.patient_register, name="patient_register"),
    url(r'^patient_panel$', views.patient_panel, name="patient_panel"),
    url(r'^patient_change_infos$', views.patient_change_infos, name="patient_change_infos"),

    url(r'^doctor_register$', views.doctor_register, name="doctor_register"),
    # url(r'^doctor_login$', views.doctor_login, name="doctor_login"),
    url(r'^doctor_panel$', views.doctor_panel, name="doctor_panel"),
    url(r'^doctor_change_infos$', views.doctor_change_infos, name="doctor_change_infos"),

    url(r'^get_doctor$', views.get_doctor, name="get_doctor"),

    url(r'^get_all_doctors$', views.get_all_doctors, name="get_all_doctors"),
    url(r'^add_comment$', views.add_comment, name="add_comment"),
    ]
