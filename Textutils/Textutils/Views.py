#I have created this file - Harsh
from django.http import HttpResponse
def index(request): #the django is automatically passing an argument call request, so we have to give that argument to our python function
    # return HttpResponse("Hello Harsh")
    #This can be used as html as well
    return HttpResponse("<h1>Harsh</h1>")

def about(request): #the django is automatically passing an argument call request, so we have to give that argument to our python function
    return HttpResponse("about Harsh")