from django.http import Http404
from django.shortcuts import  render,redirect
from .models import teacher
from django.contrib.auth import authenticate, login
from .forms import  UserForm

def index(request):
    all_teachers = teacher.objects.all()
    return render(request,'attendence/index.html',{'all_teachers' : all_teachers})


def detail(request, teacher_id):
    try:
        Teacher =teacher.objects.get(pk=teacher_id)
    except teacher.DoesNotExist:
        raise Http404("Not Exist")
    return render(request,'attendence/detail.html',{'Teacher' : Teacher})

