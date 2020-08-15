from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Quiz(models.Model):
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=30, unique=True)
    quiz_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.quiz_text


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_answer = models.BooleanField()

    def __str__(self):
        return self.choice_text
