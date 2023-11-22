from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
import urllib.request
import json
def index(request):



    api_json = urllib.request.urlopen('https://api.breakingbadquotes.xyz/v1/quotes').read()
    api_dict = json.loads(api_json)
    quotes = api_dict[0]['quote']


    author = api_dict[0]['author']

    context = {
        'api_dict':api_dict,
        "quotes":quotes,
        "author":author,

    }







    return render(request,'index.html',context)

