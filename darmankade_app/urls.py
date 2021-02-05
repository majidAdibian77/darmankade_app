from django.conf.urls import url
from darmankade_app import views
# from meeting_app.views import OAuth2CallBack

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^patient_register$', views.patient_register, name="patient_register"),
    url(r'^patient_login$', views.patient_login, name="patient_login"),
    url(r'^patient_panel$', views.patient_panel, name="patient_panel"),
    url(r'^patient_change_infos$', views.patient_change_infos, name="patient_change_infos"),
    ]