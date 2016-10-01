from django.http import HttpResponse
import os

def index(request):
    file = open(os.getcwd()+'/sathya/chatPage.html','r')
    return HttpResponse(file.read())
