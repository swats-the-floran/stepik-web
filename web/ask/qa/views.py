from django.shortcuts import render
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def root(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def login(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def signup(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def question(request, id, *args, **kwargs):
    return render(request, 'qa/basic.html')


def ask(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def popular(request, *args, **kwargs):
    return render(request, 'qa/basic.html')


def new(request, *args, **kwargs):
    return render(request, 'qa/basic.html')
