from django.shortcuts import render
import requests

def index(request):
    api_url = 'https://quoteapi.pythonanywhere.com/random'

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        quote = data["Quotes"][0]["quote"]
        author = data["Quotes"][0]["author"]
        if author == 'Null':
            author = 'Author is unknown!'
        return render(request, 'index.html', {'quote': quote, 'author': author})
    else:
        error_message = "Failed to fetch data from the API"
        return render(request, 'index.html', {'error_message': error_message})
