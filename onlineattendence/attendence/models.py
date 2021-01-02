from django.db import models


class teacher(models.Model):
    t_id = models.IntegerField(default=1)
    name = models.CharField(max_length= 150)
    email = models.CharField(max_length= 100)
    password = models.CharField(max_length= 50)



    def __str__(self):
        return 'T-ID:'+str(self.t_id) +' NAME :' + str(self.name)

class Course(models.Model):
    Course_code = models.CharField(max_length=10)
    Title = models.CharField(max_length=100)
    Semester = models.CharField(max_length=30)
    def __str__(self):
        return str(self.Title)

class Teaches(models.Model):
    t_id= models.ForeignKey(teacher,on_delete='CASCADE')
    Course_code = models.ForeignKey(Course, on_delete='CASCADE')
    Section = models.CharField( default=0 ,max_length=10)
    def __str__(self):
        return str(self.t_id)+' Course:'+str(self.Course_code)

class Attendence(models.Model):

    t_id = models.ForeignKey(teacher, on_delete='CASCADE')
    Course_code = models.ForeignKey(Course, on_delete='CASCADE')
    s_id = models.IntegerField(default=1)
    section = models.CharField(max_length=10)
    total = models.IntegerField(default=0)

    def __str__(self):
        return 'ID :'+ str(self.s_id) + ' SEC:' +str(self.section) + ' Total:' + str(self.total)

