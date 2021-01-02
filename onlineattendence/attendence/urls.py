from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'attendence'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<teacher_id>[0-9]+)/$', views.detail, name='detail'),

    ]
