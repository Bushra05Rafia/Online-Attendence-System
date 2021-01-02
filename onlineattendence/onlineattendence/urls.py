from django.urls import path
from django.contrib import admin
from django.conf.urls import include,url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addclass/', views.addclass),
    path('present/', views.present),
    url(r'users/', include('users.urls')),
    url(r'attendence/',include('attendence.urls')),

    ]