from django.contrib import admin

from . models import Category, Quiz, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category)
