from django.shortcuts import render
from .models import *

#for genric
from django.views.generic import ListView


# def homePage(r):
#     data = {
#         "students": StudentsRecord.objects.all()
#     }

#     return render(r, "studentrecords_list.html", data)

class StudentView(ListView):
    model = StudentsRecord