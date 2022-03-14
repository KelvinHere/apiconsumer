from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://46.101.13.65:8000/word')
    api_result = response.json()
    template = "home/index.html"
    context = {
        'api_result': api_result
    }
    return render(request, template, context)
