from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return render(request,'frontend_todo/list.html' )
