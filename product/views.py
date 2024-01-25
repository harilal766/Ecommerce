from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/search"

    querystring = {"keyword":"iphone","country":"US","category":"aps"}

    headers = {
	"X-RapidAPI-Key": "bef905616emsh584c0cf3a3b0cc6p1373d0jsn8f7797e343dd",
	"X-RapidAPI-Host": "amazon-product-reviews-keywords.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return render(request,'home.html',{'prod':response.json()}) 

