#Exercise1:Personal Navigator.
from django.http import HttpResponse

def index(request):
    return HttpResponse("""<h1>Harsh</h1> <a href = "https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django CodeWithHarry </a>""")