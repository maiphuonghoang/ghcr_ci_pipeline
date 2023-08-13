from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Viewers! We are testing how traffic is split")
