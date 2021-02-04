from django.conf.urls import url
from darmankade_app import views
# from meeting_app.views import OAuth2CallBack

urlpatterns = [
    url(r'^$', views.home, name="home"),
    ]