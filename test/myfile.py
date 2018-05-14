import csv
import psycopg2
import psycopg2.extras

hostname = '35.185.2.81'
username = 'postgres'
password = 'simpy1120'
database = 'simpy'
port= '5432'

csv_file = open('myfile.csv')
csv_reader = csv.reader(csv_file,delimiter=',')
next(csv_reader)

for row in csv_reader:
	name,email,location = row
	print(name,email,location)

	try:
		connection = psycopg2.connect('dbname={} host={} port={} user={} password={}'.format(database, hostname, port, username, password))
		cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		query = ("""Insert into public.user_email values(nextval('email_user'),'{}','{}','{}')""".format(email,name,location))
		cursor.execute(query)
		connection.commit()
		cursor.close()
		connection.close()
	except psycopg2.OperationalError:
		raise
		print "Connection Error. Please Check Postgres Credentials or Settings."

csv_file.close()