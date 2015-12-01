from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import *

def index(request):
    context = {
        'latest_question_list': Question.objects.order_by('-pub_date'),
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return render(request, 'polls/detail.html', {
            'question' : get_object_or_404(Question, id = question_id)
        })

def results(request, question_id):
    return render(request, 'polls/result.html', {
            'question' : get_object_or_404(Question, id = question_id)
        })

def vote(request, question_id):
    p = get_object_or_404(Question, id = question_id)
    try:
        selected_choice = p.choice_set.get(id = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : p,
            'error_message' : 'You didn\' select a correct choice',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))
