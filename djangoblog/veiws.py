from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('Hi this is test!')
    return render(request,'about.html')

def home(request):
    # return HttpResponse('Home page')
    return render(request,'home.html')