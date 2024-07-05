from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('<h1 style = "color:blue;text-align:center;backgroud-color: black">Hello Fboy</h1 ><br><h2 style = "color:blue;text-align:center">This world will f you</h2>')
