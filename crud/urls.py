
from django.contrib import admin
from django.urls import path
from students.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentView.as_view(), name="homepage"),
]
