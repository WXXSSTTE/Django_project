from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request):
    return render(request, 'main/first.html')

def about(request):
    return render(request, 'main/about.html')

def timer(request):
    return HttpResponse("Таймер")

def schedule(request):
    return HttpResponse("Расписание")

def progress(request):
    return HttpResponse("Прогресс")