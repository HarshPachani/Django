from django.http import HttpResponse
def readIt(request):
    try:
        with open("1.txt") as file:
            data = file.readlines()
            d = data[0]
    except Exception as e:
        print(e)
    return HttpResponse("Harsh")
