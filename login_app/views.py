

from django.http import *
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import os,json


def userLogin(request):
	return render(request,'login_app/login.html')

def authenticateUser(request):
	print 'request',request
	print 'this is request method data',request.method
	print 'this is request post data', request.POST
	if request.method == 'POST' and request.is_ajax():
		print request.POST
		if request.POST.get('action') == 'login_user':
			
			email = request.POST.get('email',None)
			password = request.POST.get('password',None)

			print email,password

			try:
				user = authenticate(username=email, password=password)
				print user
				print user.is_authenticated()
				if user and user.is_authenticated():
					if user.is_active:
						login(request, user)
						return HttpResponse(json.dumps({'status':'login_success'}), content_type='application/json')
					else:
						return HttpResponse(json.dumps({'status':'unverified_user'}), content_type='application/json')
				else:
					return HttpResponse(json.dumps({'status':'does_not_exist'}), content_type='application/json')
			except:
				raise
				return HttpResponse(json.dumps({'status':'does_not_exist'}), content_type='application/json')

def privacy_view(request):
	return render(request,'login_app/privacy.html')


def signup(request):
	
	return render(request,'login_app/sign_up.html')

def registeruser(request):
	print 'i am get called'
	print request
	print request.POST
	if request.method == 'POST' and request.is_ajax():

		if request.POST.get('action') == 'register_user':

			username = request.POST.get('username',None)
			email = request.POST.get('email',None)
			password = request.POST.get('password',None)

			print username,email,password

			user = User.objects.create_user(username = username,email = email, password = password)

			user.save()

	return HttpResponse(json.dumps({'register':'success'}),content_type = 'application/json')

@login_required(login_url = '/')
def user_logout(request):
	if request.method == 'GET':
		logout(request)
	return redirect('/')

	
