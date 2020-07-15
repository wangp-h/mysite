from django.shortcuts import render, HttpResponse


# Create your views here.
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    return HttpResponse('hello, Django')
