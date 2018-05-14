from django.shortcuts import render
from django.http import *
from django.http import HttpResponse

def Homepage(request):
	return render(request,'howdy/homepage.html')
