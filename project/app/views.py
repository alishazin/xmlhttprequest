from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home.html', {})

def get_request(request):
    return HttpResponse("Hello World!")

def post_request(request):
    print(request.POST)
    return HttpResponse("POST request")