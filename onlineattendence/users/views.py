from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import addclass

def indexView(request):
    return render (request,'index.html')
@login_required
def dashboardView(request):
    return render (request,'dashboard.html')
def addclass(request):
    if (request.method == "POST"):
        x1 = request.POST.get("ccode")
        x2 = request.POST.get("sec")
        x3 = request.POST.get("sem")
        obj = addclass(Course_code=x1, section=x2, semister=x3)
        obj.save()
        return render(request, "addclass.html")
    else:
        return render(request, "dashboard.html")

def present(request):
    return render(request,"present.html")
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

