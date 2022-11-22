#Exercise1:Personal Navigator.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Harsh</h1>")