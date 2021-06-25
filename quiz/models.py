from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 35)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 35)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Year(models.Model):
    year_number = models.IntegerField(default=1, null=True)

    def __str__(self):
        return str(self.year_number)
    
class Section(models.Model):
    name = models.CharField(max_length = 1)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=35)
    School = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null = True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, blank = True, null = True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE, blank = True, null = True)
    year = models.ForeignKey(Year,on_delete=models.CASCADE, blank = True, null = True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank = True, null = True)


    def __str__(self):
        return self.Name


class Subject(models.Model):
    code = models.CharField(max_length=10, blank = True, null = True, unique = True)
    Name = models.CharField(max_length=100)
    school = models.ForeignKey(School,on_delete=models.CASCADE, blank = True, null = True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, blank = True, null = True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE, blank = True, null = True)
    year = models.ForeignKey(Year,on_delete=models.CASCADE, blank = True, null = True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.Name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=35)
    Subject = models.ManyToManyField(Subject, blank = True)
    
    def __str__(self):
        return self.Name

class Quiz(models.Model):
    Description = models.CharField(max_length=200)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    Date_of_publish = models.DateTimeField(auto_now_add=True, null=True)
    Starting_Time = models.DateTimeField(null=True)
    Ending_Time = models.DateTimeField(null=True)
    Attendance_required = models.IntegerField(default=75, null=True)

    def __str__(self):
        return str(self.Description)
        
    
class Question(models.Model):
    Question_Text = models.CharField(max_length=500)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100, blank=True)
    Option4 = models.CharField(max_length=100, blank=True)
    Answer = models.CharField(max_length=100)
    QuizID = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Question_Text)

class Attendance(models.Model):
    Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Present = models.IntegerField()
    Total_Attendance = models.IntegerField()

    def __str__(self):
        return str(self.Name) + " -- " + str(self.Subject)

class QuizScore(models.Model):
    Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Marks_Obtained = models.PositiveIntegerField()
    Max_Marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Name) + " -- " + str(self.Quiz)

    