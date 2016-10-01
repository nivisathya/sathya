from django.http import HttpResponse


def index(request):
    file = open('/home/nivedhita/sathya/chatbot/sathya/chatPage.html','r')
    return HttpResponse(file.read())
