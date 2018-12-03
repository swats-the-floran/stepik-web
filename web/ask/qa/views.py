from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Question, Answer
from .forms import AskForm, AnswerForm


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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(qst.get_url())
    else:
        form = AnswerForm(initial={'question': qst.id})
    context = {
        'question': qst,
        'form': form,
    }
    return render(request, 'qa/question_detail.html', context=context)


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()  # probably None type can come here
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', context={'form': form})



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
