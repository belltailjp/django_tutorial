from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import *

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse('Detail of %s' % Question.objects.get(id = question_id))

def results(request, question_id):
    return HttpResponse('Results of %s' % Question.objects.get(id = question_id))

def vote(request, question_id):
    return HttpResponse('Votes of %s' % Question.objects.get(id = question_id))
