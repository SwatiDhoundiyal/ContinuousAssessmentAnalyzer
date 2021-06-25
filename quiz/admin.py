from django.contrib import admin
from quiz.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(QuizScore)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Section)

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('Date_of_publish',)

admin.site.register(Quiz,RatingAdmin)