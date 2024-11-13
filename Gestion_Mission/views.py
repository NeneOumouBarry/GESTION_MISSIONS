from django.shortcuts import render,redirect
from django.http import HttpResponse

def dashboard(request):
    return render(request, "index.html")