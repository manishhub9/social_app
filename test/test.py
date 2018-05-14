import datetime
from datetime import date, timedelta


yesterday = date.today() - timedelta(2)
tommorrow = date.today() + timedelta(2)


now = datetime.datetime.now()


print "Current date and time using str method of datetime object:"
print str(now)

print yesterday.strftime('%m-%d-%y')
print tommorrow.strftime('%m-%d-%y')
