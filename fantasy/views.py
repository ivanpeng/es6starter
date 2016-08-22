from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello World. You are at the root")


def fantasy_index(request):
    return HttpResponse("Hello World. You are at the fantasy root.")


def js_test(request):
    return render(request, "js_test.html")
