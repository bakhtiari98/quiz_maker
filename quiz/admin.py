from django.contrib import admin

from . models import Category, Quiz, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'create_date', 'update_date', 'score', 'active']
    list_editable = ['active']
    inlines = [ChoiceInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ['quiz_text', 'category_to_str', 'create_date', 'update_date', 'active']
    list_editable = ['active']
    inlines = [QuestionInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_editable = ['active']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
