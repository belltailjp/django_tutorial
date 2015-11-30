from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import *

def index(request):
    context = {
        'latest_question_list': Question.objects.order_by('-pub_date'),
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse('Detail of %s' % Question.objects.get(id = question_id))

def results(request, question_id):
    return HttpResponse('Results of %s' % Question.objects.get(id = question_id))

def vote(request, question_id):
    return HttpResponse('Votes of %s' % Question.objects.get(id = question_id))
