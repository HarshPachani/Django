from django.http import HttpResponse
def index(request):
    return HttpResponse("Home")

def removePunc(request):
    return HttpResponse("Removepunc")

def capFirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("new line remover")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount")