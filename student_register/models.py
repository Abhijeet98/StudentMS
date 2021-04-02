from django.db import models

# Create your models here.
class Course (models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    stud_id = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=10)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)