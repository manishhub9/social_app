from forex_python.converter import CurrencyRates
import csv

c = CurrencyRates()

fileObject = open('currency.csv')
csv_reader = csv.reader(fileObject,delimiter=',')

# For skip the header
next(csv_reader) 

for each in csv_reader:
	Cname,Ccode = each

	print Ccode
	try:
		data = c.get_rates(Ccode)
		print data
	except:
		print 'Not available for ', Ccode
		pass

	
	 

