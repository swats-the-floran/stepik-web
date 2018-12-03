from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # self._user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question_obj = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            question_obj = None
        return question_obj

    def clean(self):
        return self.cleaned_data

    def save(self):
        return Answer.objects.create(**self.cleaned_data)
