from django.http import HttpResponse
from queryParser import processLanguage
import os
import wikipedia

def index(request):
    file = open(os.getcwd()+'/sathya/chatPage.html','r')
    return HttpResponse(file.read())

def ask(request):
    question = request.GET.get('q', '')
    return HttpResponse(answer(question))

def answer(ques):
    ques = " ".join(processLanguage(ques))
    title = wikipedia.search(ques)
    return wikipedia.summary(title[0], sentences=3)
