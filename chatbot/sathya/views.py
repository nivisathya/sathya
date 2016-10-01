from django.http import HttpResponse
import os

def index(request):
    file = open(os.getcwd()+'/sathya/chatPage.html','r')
    return HttpResponse(file.read())

def ask(request):
    question = request.GET.get('q', '')
    return HttpResponse(question)
