from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Enrollment, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    # list_display = ['title']
    list_display = ('order', 'title', 'course')
    

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'grade', 'lesson')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'is_correct', 'question')


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission)

