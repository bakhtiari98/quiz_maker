from django.db import models


# Managers
class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class CategoryManager(ActiveManager):
    pass


class QuizManager(ActiveManager):
    pass


class QuestionManager(ActiveManager):
    pass


# Models
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Quiz(models.Model):
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=30, unique=True)
    quiz_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])

    category_to_str.short_description = "Categories"

    def __str__(self):
        return self.quiz_text

    objects = QuizManager()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

    objects = QuestionManager()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_answer = models.BooleanField()

    def __str__(self):
        return self.choice_text
