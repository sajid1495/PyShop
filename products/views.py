from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, this is the products index page.")


def new_product(request):
    return HttpResponse("Hello, this is the new product page.")
