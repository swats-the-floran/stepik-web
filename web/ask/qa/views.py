from django.shortcuts import render
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def root(request, *args, **kwargs):
    return HttpResponse(status=404)


def login(request, *args, **kwargs):
    return HttpResponse(status=404)


def signup(request, *args, **kwargs):
    return HttpResponse(status=404)


def question(request, id, *args, **kwargs):
    print(id)
    print(type(id))

    return HttpResponse(id)


def ask(request, *args, **kwargs):
    return HttpResponse(status=404)


def popular(request, *args, **kwargs):
    return HttpResponse(status=404)


def new(request, *args, **kwargs):
    return HttpResponse(status=404)
