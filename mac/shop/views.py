from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Index Shop")
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("We re at about")


def contact(request):
    return HttpResponse("We re at about")

def tracker(request):
    return HttpResponse("We re at tracker")

def productView(request):
    return HttpResponse("We re at prodView")

def checkout(request):
    return HttpResponse("We re at checkout")

def search(request):
    return HttpResponse("We are searching")
