from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *


# Create your views here.
def first(request):
    return render(request, 'first_page.html')


