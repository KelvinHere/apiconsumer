from django.shortcuts import render

def home(request):
    template = "home/index.html"
    return render(request, template)
