from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def student(request):
    return HttpResponse('This is the student login Screen')
def acclog(request):
    return render(request,'account_log.html')
