import json
from django.shortcuts import render, HttpResponse
import requests

def home(request):
    try:
        raise ValueError # Force value error exception
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
    ''' Get random word and return as JSON data for use with ajax '''
    if request.method == 'GET':
        try:
            json_response = requests.get('http://46.101.13.65:8000/word')
            api_result = json.dumps(json_response.json())
        except ValueError:
            api_result = json.dumps({
                            "id": '1',
                            "word": "SERVER ERROR",
                            "meaning": "PLEASE TRY AGAIN LATER"
                        })
        

        return HttpResponse(api_result, content_type='application/json')

          
def word_by_pk(request):
    ''' Get random word and return as JSON data for use with ajax '''
    if request.method == 'GET':
        pk = request.GET['pk']
        try:
            json_response = requests.get(f'http://46.101.13.65:8000/word/{pk}')
            api_result = json.dumps(json_response.json())
            # If this key does not exist generate error message
            if api_result == '{"detail": "Not found."}':
                api_result = '{"Error": "Word with this PK does not exist"}'
        except ValueError:
            api_result = json.dumps({
                            "id": '1',
                            "word": "SERVER ERROR",
                            "meaning": "PLEASE TRY AGAIN LATER"
                        })

        return HttpResponse(api_result, content_type='application/json')





    
