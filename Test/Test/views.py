from django.http import HttpResponse

def showName(request):
    return HttpResponse("Harsh")