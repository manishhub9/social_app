from django.shortcuts import render
from django.http import *
from django.http import HttpResponse


def dashboard(request):
	return render(request,'dashboard/dashboard.html')

# Create your views here.
