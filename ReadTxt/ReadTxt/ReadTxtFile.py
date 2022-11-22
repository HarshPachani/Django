from django.http import HttpResponse
def readIt(request):
    with open("1.txt") as file:
        data = file.readlines()
        d = data
    return HttpResponse(d)
