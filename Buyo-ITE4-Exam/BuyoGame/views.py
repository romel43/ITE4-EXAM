import http
from django.http import HttpResponse
from django.shortcuts import render
import random
def index(request):

    return render(request, 'index.html')
def result(request):
    params = {}
    choosen = request.GET['choice']

    comp = random.choices(["R", "P", "S"])
    device = comp[0]

    
    if device == choosen:
        params['device'] = 'SAME AS YOU'
        params['result'] = "THIS GAME IS TIED ." 
    elif device == 'R':
        params['device'] = 'ROCK'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED ."
        elif choosen == 'P':
            params['result'] = "Result : You Win ."
        else:
            params['result'] = "Result : Computer Win ."
    elif device == 'S':
        params['device'] = 'STONE'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED ."
        elif choosen == 'P':
            params['result'] = "Result : Computer Win ."
        else:
            params['result'] = "Result : You Win ."
    elif device == 'P':
        params['device'] = 'PAPER'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED ."
        elif choosen == "S":
            params['result'] = "Result : You Win ."
        else:
            params['result'] = "Result : Computer Win ."
            
    return render(request, 'index.html', params)
