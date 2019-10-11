import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def new__search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search': search}
    return render(request, 'my_app/new__search.html', stuff_for_frontend)


