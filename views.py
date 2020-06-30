from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def contacto(request):
    return HttpResponse("pandemia news 2020")
