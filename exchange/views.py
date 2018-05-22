from django.shortcuts import render
from django.http import HttpResponse
from io import StringIO
import json
import csv
from models import Country



def index(request):
	return render(request,'exchange/uploadform.html')

def upload_data(request):
	fileData =  request.FILES.get('csv_file')
	fileObject = fileData
	csv_reader = csv.reader(fileObject,delimiter=',')

	next(csv_reader) 

	for each in csv_reader:
		Cname,Ccode = each

		if Cname != '' and Ccode != '':
			print Cname,Ccode
			Country.objects.create(c_name=Cname,c_code=Ccode)
		else:
			print 'Cname',Cname
			print 'Ccode',Ccode
			
	return HttpResponse(json.dumps({}),content_type='application/json')
