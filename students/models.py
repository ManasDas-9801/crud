from django.db import models

class StudentsRecord(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name