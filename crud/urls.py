
from django.contrib import admin
from django.urls import path
from students.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentView.as_view(), name="homepage"),
    path('insert/', StudentFormView.as_view(), name="insertPage"),
    path('<pk>/student-delete/', DeleteStudentView.as_view(), name="deleteStudent"),
    path('<pk>/student-edit/', StudentEditView.as_view(), name="StudentEditView"),
]
