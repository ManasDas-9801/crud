from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

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

class LoginView(FormView):
    template_name = "./login.html"
    form_class = AuthenticationForm
    success_url = "/"
    
    def post(self,request):
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("homepage")
            else:
                return HttpResponse("User is not activated")
        else:
            return HttpResponse("Invalid user name and password")
        return HttpResponse("Login Checking")
    
class LogoutView(View):
    def get(self,r):
        logout(r)
        return redirect("homepage")
    
