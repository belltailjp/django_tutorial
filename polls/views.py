from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from polls.models import *

def index(request):
    context = {
        'latest_question_list': Question.objects.order_by('-pub_date'),
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    return HttpResponse('Results of %s' % Question.objects.get(id = question_id))

def vote(request, question_id):
    return HttpResponse('Votes of %s' % Question.objects.get(id = question_id))
