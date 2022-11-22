from django.http import HttpResponse

def showName(request):
    name = "Harsh2"
    return HttpResponse(name)