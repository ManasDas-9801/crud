from django.shortcuts import render
from .models import *
from .forms import *
#for genric
from django.views.generic import ListView,FormView


# def homePage(r):
#     data = {
#         "students": StudentsRecord.objects.all()
#     }

#     return render(r, "studentrecords_list.html", data)

class StudentView(ListView):
    model = StudentsRecord


class StudentFormView(FormView):
    template_name = "./insert.html"
    form_class = StudentForm
    success_url = "/"
    def form_valid(self, form):
         form.save()
         return super().form_valid(form)