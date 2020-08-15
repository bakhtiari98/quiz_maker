from django.shortcuts import render, get_object_or_404

from . models import Quiz, Category


def index(request):
    quizzes = Quiz.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    return render(request, 'quiz/index.html', {'quizzes': quizzes, 'categories':categories})


def detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, 'quiz/detail.html', {'quiz': quiz})
