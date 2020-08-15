from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=30, unique=True)
    quiz_text = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.quiz_text


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    create_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    score = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.TextField()
    is_answer = models.BooleanField()

    def __str__(self):
        return self.choice_text
