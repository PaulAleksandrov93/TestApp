from django.http import HttpResponse
from django.shortcuts import render
from .models import CMenu

# Create your views here.
def menu(request):
    return render(request, 'base.html')