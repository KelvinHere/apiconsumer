from json import JSONDecodeError
from django.shortcuts import render
import requests

def home(request):
    try:
        response = requests.get('http://46.101.13.65:8000/word')
        api_result = response.json()
    except ValueError:
        api_result = {
                        "id": '1',
                        "word": "SERVER ERROR",
                        "meaning": "PLEASE TRY AGAIN LATER"
                     }

    template = "home/index.html"
    context = {
        'api_result': api_result
    }
    return render(request, template, context)

    





    
