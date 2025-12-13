from django.db import models

class Career(models.Model):
   code = models.CharField(max_length=3, primary_key=True)
   name = models.CharField(max_length=50)
   duration = models.PositiveSmallIntegerField(default=5)
   
   def __str__(self):
      txt = "{0} (Duration: {1} year(s))"
      return txt.format(self.name, self.duration)

class Student(models.Model):
   idCard = models.CharField(max_length=11, primary_key=True)
   paternalSurname = models.CharField(max_length=35)
   maternalSurname = models.CharField(max_length=35)
   Names = models.CharField(max_length=35)
   dateOfBirth = models.DateField()
   sex = [
      ("F", "Female"),
      ("M", "Male")
   ]
   sex = models.CharField(max_length=1, choices=sex, default="F")
   career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
   validity = models.BooleanField(default=True)
   
   def fullName(self):
      txt = "{0} {1}, {2}"
      return txt.format(self.paternalSurname, self.maternalSurname, self.Names)


   def __str__(self):
      txt = "{0} /  Career: {1} / {2}"
      if self.validity:
         statusStudent = "CURRENT"
      else:
         statusStudent = "ON LOW"
      return txt.format(self.fullName(), self.career, statusStudent)


class Course(models.Model):
   code = models.CharField(max_length=6, primary_key=True)
   name = models.CharField(max_length=30)
   credits = models.PositiveSmallIntegerField()
   teacher = models.CharField(max_length=100)

   def __str__(self):
      txt = "{0} ({1}) - Teacher: {2}"
      return txt.format(self.name, self.code, self.teacher)


class Enrollment(models.Model):
   id = models.AutoField(primary_key=True)
   student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
   course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
   dateRegistration = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
      txt = "Enrollment ID: {0} - Student: {1} - Course: {2} - Date: {3}"
      return txt.format(self.id, self.student.fullName(), self.course.name, self.dateRegistration)
   