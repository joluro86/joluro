from django.shortcuts import render

def index(request):
    return render(request, "sale/index.html")

def detail(request):
    return render(request, "sale/detail.html")

