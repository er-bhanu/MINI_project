from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

SESSION = [
        ('Tutorial', 'Tutorial'),
        ('Lecture', 'Lecture'),
        ('Lab', 'Lab'),
        ('Discussion', 'Discussion'),
        ('Presentation', 'Presentation'),
    ]
class Department(models.Model):
    DepartmentName = models.CharField(max_length=100,primary_key=True)
    HeadOfDepartment = models.CharField(max_length=100)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Department"
      verbose_name_plural = "Department"
    def __str__(self):
        return self.DepartmentName

class Instructor(AbstractUser):
    FirstName = models.CharField(max_length=100,null=True)
    MiddleName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=100,null=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Instructor"
      verbose_name_plural = "Instructor"
    def __str__(self):
        return self.username

class TimeTableMain(models.Model):
    YearOfStudy = models.CharField(max_length=9)
    Programme = models.CharField(max_length=100,primary_key=True,editable=True)
    Semister  = models.CharField(max_length=100)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Programme
  
class CourseName(models.Model):
    Course = models.CharField(max_length=5)
    CourseCode = models.CharField(max_length=100,primary_key=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    CourseDescription= models.CharField(max_length=200)
    def __str__(self):
        return self.Course
    class Meta:
        unique_together = (('Course', 'CourseCode'),)

class Venue(models.Model):
    Venue = models.CharField(max_length=50,primary_key=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Venue
 

class TimeTable(models.Model):
    CourseName = models.ForeignKey(CourseName, on_delete=models.CASCADE)
    Instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)   
    Venue = models.ForeignKey(Venue,on_delete=models.CASCADE) 
    Timestart = models.TimeField()
    TimeEnd = models.TimeField()
    Day = models.CharField(max_length=100, choices=DAY_CHOICES)
    Programme=models.ForeignKey(TimeTableMain,on_delete=models.CASCADE)   
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    SessionType= models.CharField(max_length=100, choices=SESSION)
     