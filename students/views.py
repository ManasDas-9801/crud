from django.shortcuts import render
from .models import *
# from .forms import *
#for genric
from django.views.generic import *

# def homePage(r):
#     data = {
#         "students": StudentsRecord.objects.all()
#     }

#     return render(r, "studentrecords_list.html", data)

class StudentView(ListView):
    model = StudentsRecord


class StudentFormView(CreateView):
    template_name = "./insert.html"
    model = StudentsRecord
    fields = "__all__"
    success_url = "/"
    def form_valid(self, form):
         form.save()
         return super().form_valid(form)
    
class DeleteStudentView(DeleteView):
    model = StudentsRecord
    success_url = "/"
    template_name = "./delete.html"

class StudentEditView(UpdateView):
    model = StudentsRecord
    fields = "__all__"
    success_url = "/"
    template_name = "./insert.html"