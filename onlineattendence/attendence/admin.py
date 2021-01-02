from django.contrib import admin
from .models import teacher,Course,Teaches,Attendence

admin.site.register(teacher)
admin.site.register(Course)
admin.site.register(Teaches)
admin.site.register(Attendence)