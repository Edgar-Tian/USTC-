from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context={}
    context['hello']='大物实验'
    return render(request,'Hello.html',context)
