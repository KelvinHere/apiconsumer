from json import JSONDecodeError, dumps
from django.shortcuts import render, HttpResponse
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

def random_word(request):
    ''' Get random word and return as JSON data '''
    print('######################### api response')
    if request.method == 'GET':
        try:
            json_response = requests.get('http://46.101.13.65:8000/word')
            api_result = dumps(json_response.json())
        except ValueError:
            api_result = dumps({
                            "id": '1',
                            "word": "SERVER ERROR",
                            "meaning": "PLEASE TRY AGAIN LATER"
                        })
        

        return HttpResponse(api_result, content_type='application/json')
            

        





    
