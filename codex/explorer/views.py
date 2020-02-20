from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse("Hello, world. You are at Codex Index.")

def detail(request, question_id):
    response = "You'r looking at the question %s."
    return (response % question_id)

def results(request, question_id):
    return HttpResponse("You'r looking at the results of the questopms %s."%question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

