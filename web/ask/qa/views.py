from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def root(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def login(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def signup(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def question(request, pk, *args, **kwargs):
    qst = get_object_or_404(Question, pk=pk)
    ans = Answer.objects.filter(question=qst)
    context = {
        'question': qst,
        'answers': ans,
    }
    return render(request, 'qa/question_detail.html', context=context)


def ask(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def popular(request, *args, **kwargs):
    qst = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(qst, 10)
    paginator.base_url = '?page='
    page = paginator.page(page)
    context = {
        'page_title': 'Popular Questions:',
        'paginator': paginator,
        'page': page,
        'questions': qst,
    }
    return render(request, 'qa/question_list.html', context=context)


def new(request, *args, **kwargs):
    qst = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(qst, 10)
    paginator.base_url = '?page='
    page = paginator.page(page)
    context = {
        'page_title': 'New Questions:',
        'paginator': paginator,
        'page': page,
        'questions': qst,
    }
    return render(request, 'qa/question_list.html', context=context)
