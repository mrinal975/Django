from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
def home(request):
    return render(request, 'index.html', {'name':'mrinal'})

def add(request):
    first = int(request.GET['first'])
    second = int(request.GET['second'])
    result = first + second
    return render(request, 'result.html', {'result':result})
