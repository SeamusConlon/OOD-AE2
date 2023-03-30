from django.shortcuts import render
from django.http import HttpResponse
from httprequests.models import HexFactory

# Create your views here.

def home(request):
    return render(request, "httprequests/home.html")

def hexresult(request):
    red = request.GET.get('red')
    green = request.GET.get('green')
    blue = request.GET.get('blue')
    h = HexFactory(red,green,blue)
    return render(request, "httprequests/hexresult.html", {'result':h.factory_result()})